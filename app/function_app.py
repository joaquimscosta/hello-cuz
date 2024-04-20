import azure.functions as func
import json
import os
import logging
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email
from openai import OpenAI
from dotenv import load_dotenv

app = func.FunctionApp()

load_dotenv()

# Scope for read-only access to the calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = os.path.join(
    os.path.dirname(__file__), 'service-account-file.json')
CALENDAR_ID = os.getenv('CALENDAR_ID')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
FROM_EMAIL = os.getenv('FROM_EMAIL')
EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS').split(',')


# {second} {minute} {hour} {day} {month} {day of the week}
# execute this function every first of the month
@app.timer_trigger(schedule="0 0 0 1 * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=True)
def monthly_event_notifier(myTimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function executed.')
    process_notification()


def process_notification():
    now = datetime.datetime.now()
    logging.info(f"current time is {now}")
    year = now.year
    month = now.month
    service = authenticate_google_calendar()

    # Get this months events from Google calendar
    events = get_events(service, year, month)

    # Generate a prompt to input in GPT
    prompt = create_prompt(events)
    logging.info(prompt)

    # Tell GPT to generate an email based on this prompt
    # {subject:"","content":""}
    email = generate_email_content(prompt)
    logging.info(f"generated email by GPT = {email}")

    if email == None:
        logging.info('No email generated')
        return
    # Send email
    notify(json.loads(email))


def authenticate_google_calendar():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build('calendar', 'v3', credentials=credentials)
    return service


def get_events(service, year, month):
    # Calculate the start and end of the specified month
    start_date = datetime.datetime(year, month, 1)
    end_date = datetime.datetime(
        year, month + 1, 1) if month < 12 else datetime.datetime(year + 1, 1, 1)

    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=start_date.isoformat() + 'Z',
                                          timeMax=end_date.isoformat() + 'Z', singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    logging.info(f"Found events {len(events)} ")
    return events


def create_prompt(events):
    content = """Write a fun, friendly and concise email to my cousin informing about the events planned for this month.
    Have each event contained in a bullet point, add fun emoji. 
    The email should start with 'Hey Family', and the sender is 'Rodrigues Cousins'. 
    End the email with an motivational quote. 
    The email content should be in HTML and the prompt response should be returned as JSON including 'subject' and 'content'.
    Here are the list of events happening this month:\n"""
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        content += f"{start} - {event['summary']}\n"
    return content


def notify(email):
    message = Mail(
        from_email=Email(FROM_EMAIL, 'Rodrigues Cousins'),
        to_emails=EMAIL_RECIPIENTS,
        subject=email['subject'],
        html_content=email['content']
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        logging.info(response.status_code)
        logging.info(response.body)
        logging.info(response.headers)
    except Exception as e:
        logging.error(e.message)


def generate_email_content(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are an email writer assistant that writes monthly email informing about events planned for a specific month."
                },
                {
                    "role": "user",
                    "content": f"{prompt}"
                }
            ],
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(e.message)
    return None

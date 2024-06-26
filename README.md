<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/joaquimscosta/hello-cuz">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">Hello Cuz</h3>

  <p align="center">
    Hello Cuz is a simple app that sends a monthly newsletter to my family and friends talking about the events happening this month.
    <br />
    <br />
    <a href="https://github.com/joaquimscosta/hello-cuz">View Demo</a>
    ·
    <a href="https://github.com/joaquimscosta/hello-cuz/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/joaquimscosta/hello-cuz/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This goal of this project was to create a fun and engaging way to keep my family and friends updated on the events happening each month. By automating the process of generating and sending newsletters, I can ensure that everyone stays in touch.

### Built With

* [![Python][Python-shield]][Python-url] - Used to write the code for the Azure Functions.
* [![Azure Functions][AzureFunctions-shield]][AzureFunctions-url] - Used to host the application logic and trigger the newsletter generation process on a monthly basis.
* [![Google Calendar API][GoogleCalendarAPI-shield]][GoogleCalendarAPI-url] - Utilized to fetch events from the shared family calendar. This data forms the basis of the newsletter content.
* [![OpenAI][OpenAI-shield]][OpenAI-url] - Employs the capabilities of OpenAI's GPT model to generate the email content based on the events fetched from the Google Calendar API.
* [![SendGrid][SendGrid-shield]][SendGrid-url] - Responsible for the delivery of the generated newsletters via email.

Each of these components plays a crucial role in the functioning of the application, contributing to its ability to automate the process of creating and sending personalized newsletters.

<!-- GETTING STARTED -->
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.10 or later: [Download Python][DownloadPython-url]
* pip (Python package installer): pip is included as a default package in Python 3.4 and later versions.

### Installing Azure Functions Core Tools

The Azure Functions Core Tools provide a local development experience for creating, developing, testing, running, and debugging Azure Functions.

1. Install the [Azure Functions Core Tools][AzFuncCoreTools-url]. You need version 3.x of the Tools for Python development.
2. Verify that the tools are installed correctly by running the following command in your terminal:

    ```sh
    func --version
    ```

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/joaquimscosta/hello-cuz.git
   ```

2. Navigate to the project directory

   ```sh
   cd app
   ```

3. Install python packages

   ```sh
    pip install -r requirements.txt
   ```

4. Set up the required environment variables. You will need to replace 'your_value' with the actual values for your application.

    ```sh
    export GOOGLE_CALENDAR_ID='your_value'
    export OPENAI_API_KEY='your_value'
    export SENDGRID_API_KEY='your_value'
    ```

5. Run the Azure Function locally:

    ```sh
    func start
    ```

## Deploy

To deploy the application, you will need to use the Azure CLI and the Azure Functions Core Tools (func).

1. Login to your Azure account using the Azure CLI:

    ```sh
    az login
    ```

2. Navigate to the directory containing your Bicep file and deploy your infrastructure using the az deployment group create command:

    ```sh
    az deployment group create --resource-group $RESOURCE_GROUP --template-file main.bicep
    ```

3. Once your infrastructure is deployed, you can publish your function app using the func azure functionapp publish command:

    ```sh
    cd app
    func azure functionapp publish <function-app-name> --force
    ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Joaquim Costa - [LinkedIn](https://linkedin.com/in/joaquimscosta)

Project Link: [https://github.com/joaquimscosta/hello-cuz](https://github.com/joaquimscosta/hello-cuz)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/joaquimscosta/hello-cuz.svg?style=for-the-badge
[contributors-url]: https://github.com/joaquimscosta/hello-cuz/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/joaquimscosta/hello-cuz.svg?style=for-the-badge
[forks-url]: https://github.com/joaquimscosta/hello-cuz/network/members
[stars-shield]: https://img.shields.io/github/stars/joaquimscosta/hello-cuz.svg?style=for-the-badge
[stars-url]: https://github.com/joaquimscosta/hello-cuz/stargazers
[issues-shield]: https://img.shields.io/github/issues/joaquimscosta/hello-cuz.svg?style=for-the-badge
[issues-url]: https://github.com/joaquimscosta/hello-cuz/issues
[license-shield]: https://img.shields.io/github/license/joaquimscosta/hello-cuz.svg?style=for-the-badge
[license-url]: https://github.com/joaquimscosta/hello-cuz/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/joaquimscosta
[product-screenshot]: images/screenshot.png

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[AzureFunctions-shield]: https://img.shields.io/badge/Azure_Functions-0062AD?style=for-the-badge&logo=azure-functions&logoColor=white
[AzureFunctions-url]: https://azure.microsoft.com/en-us/services/functions/
[GoogleCalendarAPI-shield]: https://img.shields.io/badge/Google_Calendar_API-4285F4?style=for-the-badge&logo=google-calendar&logoColor=white
[GoogleCalendarAPI-url]: https://developers.google.com/calendar
[OpenAI-shield]: https://img.shields.io/badge/OpenAI-FF0084?style=for-the-badge&logo=openai&logoColor=white
[OpenAI-url]: https://www.openai.com/
[SendGrid-shield]: https://img.shields.io/badge/SendGrid-3B5998?style=for-the-badge&logo=sendgrid&logoColor=white
[SendGrid-url]: https://sendgrid.com/

[DownloadPython-url]: https://www.python.org/downloads/
[AzFuncCoreTools-url]: https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python

## Create a workflow identity for the GitHub repository

## Register application with Microsoft Entra ID

```sh
githubOrganizationName='joaquimscosta'
githubRepositoryName='hello-cuz'

appRegistrationDetails=$(az ad app create --display-name 'hello-cuz-workflow')
appRegistrationObjectId=$(echo $appRegistrationDetails | jq -r '.id')
appRegistrationAppId=$(echo $appRegistrationDetails | jq -r '.appId')
```

### Create federated credential

```sh
az ad app federated-credential create \
   --id $appRegistrationObjectId \
   --parameters "{\"name\":\"hello-cuz-workflow\",\"issuer\":\"https://token.actions.githubusercontent.com\",\"subject\":\"repo:${githubOrganizationName}/${githubRepositoryName}:ref:refs/heads/main\",\"audiences\":[\"api://AzureADTokenExchange\"]}"
```

## Create a resource group in Azure and grant the workflow identity access to it

```sh
resourceGroupResourceId=$(az group create --name hellocuz-rg --location eastus --query id --output tsv)

az ad sp create --id $appRegistrationObjectId
az role assignment create \
   --assignee $appRegistrationAppId \
   --role Contributor \
   --scope $resourceGroupResourceId
```

## Prepare GitHub secrets

```sh
echo "AZURE_CLIENT_ID: $appRegistrationAppId"
echo "AZURE_TENANT_ID: $(az account show --query tenantId --output tsv)"
echo "AZURE_SUBSCRIPTION_ID: $(az account show --query id --output tsv)"
```

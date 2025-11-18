# Azure OpenAI Setup Guide

This guide will help you set up and configure Azure OpenAI for use with the AI Query Assistant.

## Prerequisites

- An active Azure subscription
- Access to Azure OpenAI Service (requires application approval from Microsoft)

## Step-by-Step Setup

### 1. Get Access to Azure OpenAI Service

If you don't have access yet:
1. Visit the [Azure OpenAI Service request form](https://aka.ms/oai/access)
2. Fill out the application form
3. Wait for approval (usually takes a few days)

### 2. Create an Azure OpenAI Resource

1. Log in to [Azure Portal](https://portal.azure.com)
2. Click **"Create a resource"**
3. Search for **"Azure OpenAI"**
4. Click **"Create"**
5. Fill in the required information:
   - **Subscription**: Select your subscription
   - **Resource group**: Create new or select existing
   - **Region**: Choose a region (e.g., East US, West Europe)
   - **Name**: Give your resource a unique name
   - **Pricing tier**: Select appropriate tier (usually Standard S0)
6. Click **"Review + Create"** then **"Create"**

### 3. Deploy a Model

1. Once the resource is created, go to your Azure OpenAI resource
2. Click **"Model deployments"** or **"Go to Azure OpenAI Studio"**
3. In Azure OpenAI Studio, click **"Deployments"**
4. Click **"+ Create new deployment"**
5. Choose a model:
   - **gpt-4** (recommended for best quality)
   - **gpt-35-turbo** (faster, more economical)
   - **gpt-4-32k** (for longer context)
6. Give your deployment a name (e.g., "gpt-4-deployment")
7. Click **"Create"**

### 4. Get Your Credentials

1. In Azure Portal, go to your Azure OpenAI resource
2. Click **"Keys and Endpoint"** in the left sidebar
3. Copy the following information:
   - **KEY 1** or **KEY 2** (your API key)
   - **Endpoint** (e.g., `https://your-resource.openai.azure.com/`)
4. Note your **deployment name** from the previous step

### 5. Configure the Application

#### Option 1: Using the Streamlit UI
1. Run the application: `streamlit run app.py`
2. In the sidebar, select **"Azure OpenAI"** from the dropdown
3. Enter your credentials:
   - Azure OpenAI API Key: `[Your API Key]`
   - Azure OpenAI Endpoint: `https://your-resource.openai.azure.com/`
   - Deployment Name: `[Your deployment name]`
   - API Version: `2024-02-15-preview` (default)

#### Option 2: Using .env File
1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and set:
   ```bash
   LLM_PROVIDER=azureopenai
   AZURE_OPENAI_API_KEY=your_api_key_here
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Supported API Versions

Common Azure OpenAI API versions:
- `2024-02-15-preview` (recommended, latest features)
- `2023-12-01-preview`
- `2023-05-15`

Check [Azure OpenAI API versions](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation) for the latest.

## Common Deployment Names

When deploying models in Azure OpenAI Studio, you can use any name. Common conventions:
- `gpt-4` or `gpt4`
- `gpt-35-turbo` or `gpt35turbo`
- `gpt-4-32k` or `gpt4-32k`

**Important:** Use the exact name you chose during deployment.

## Cost Considerations

Azure OpenAI pricing is based on:
- **Token usage**: Pay per 1,000 tokens (input + output)
- **Model type**: GPT-4 is more expensive than GPT-3.5-turbo
- **Region**: Prices may vary by region

Pricing examples (as of 2024, check Azure pricing for current rates):
- GPT-3.5-turbo: ~$0.0015 per 1K input tokens, ~$0.002 per 1K output tokens
- GPT-4: ~$0.03 per 1K input tokens, ~$0.06 per 1K output tokens

## Troubleshooting

### Error: "Resource not found"
- Verify your endpoint URL is correct
- Ensure the endpoint ends with a forward slash: `https://your-resource.openai.azure.com/`

### Error: "Deployment not found"
- Check that your deployment name matches exactly what's in Azure Portal
- Deployment names are case-sensitive

### Error: "Invalid API key"
- Ensure you copied the entire API key without extra spaces
- Try regenerating the key in Azure Portal

### Error: "Quota exceeded"
- Your Azure subscription may have reached its token quota
- Check your quota limits in Azure Portal
- Request a quota increase if needed

### Error: "API version not supported"
- Try using a more recent API version
- Check the Azure OpenAI documentation for supported versions

## Rate Limits

Azure OpenAI has rate limits based on your deployment:
- **Tokens per minute (TPM)**: Varies by model and deployment
- **Requests per minute (RPM)**: Varies by model and deployment

You can view and adjust rate limits in Azure OpenAI Studio under your deployment settings.

## Security Best Practices

1. **Never commit API keys to version control**
   - Use `.env` files (already in `.gitignore`)
   - Use Azure Key Vault for production

2. **Rotate keys regularly**
   - Azure provides two keys so you can rotate without downtime

3. **Use managed identities** (for production)
   - Eliminates need to store credentials
   - Automatically managed by Azure

4. **Enable monitoring**
   - Use Azure Monitor to track usage
   - Set up alerts for unusual activity

## Additional Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure OpenAI Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)
- [Azure OpenAI Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart)
- [Azure OpenAI Studio](https://oai.azure.com/)

## Support

For Azure OpenAI issues:
- Check Azure Service Health
- Open a support ticket in Azure Portal
- Visit the [Azure AI Services community](https://techcommunity.microsoft.com/t5/azure-ai-services/bd-p/AzureAIServices)

# AI Query Assistant with CrewAI

An intelligent Streamlit application powered by CrewAI that automatically identifies query intent and routes questions to specialized AI agents.

## Features

- **Automatic Intent Classification**: Identifies whether your query is asking for a summary, comparison, or direct answer
- **Specialized Agents**: Three dedicated agents optimized for different types of queries:
  - **Summary Agent**: Provides concise overviews and summaries
  - **Compare Agent**: Delivers detailed comparisons with pros/cons
  - **Q&A Agent**: Answers specific questions with comprehensive responses
- **Multiple LLM Providers**: Supports both OpenAI and Azure OpenAI
- **Interactive UI**: Clean, user-friendly Streamlit interface
- **Powered by CrewAI**: Leverages the CrewAI framework for agent orchestration

## Architecture

```
User Query → Intent Classifier Agent → Routes to:
                                       ├── Summary Agent
                                       ├── Compare Agent
                                       └── Q&A Agent
                                              ↓
                                      Final Response
```

## Installation

1. **Clone or navigate to the project directory**

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```

   **For OpenAI:**
   Edit `.env` and configure:
   ```bash
   LLM_PROVIDER=openai
   OPENAI_API_KEY=your_actual_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

   **For Azure OpenAI:**
   Edit `.env` and configure:
   ```bash
   LLM_PROVIDER=azureopenai
   AZURE_OPENAI_API_KEY=your_azure_api_key_here
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_DEPLOYMENT=gpt-4
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to the URL shown (typically `http://localhost:8501`)

3. **Configure your LLM provider in the sidebar:**
   - Select either "OpenAI" or "Azure OpenAI"
   - Enter the required credentials
   - Alternatively, you can set these in the `.env` file

4. **Ask your question** in the text area and click Submit!

## Example Queries

### Summary Queries
- "Summarize the benefits of artificial intelligence"
- "Give me an overview of machine learning"
- "What is quantum computing in simple terms?"

### Comparison Queries
- "Compare Python and JavaScript for web development"
- "What are the differences between SQL and NoSQL databases?"
- "Compare electric cars vs gasoline cars"

### Q&A Queries
- "How does blockchain technology work?"
- "What is the capital of France?"
- "Explain photosynthesis"

## Configuration

### LLM Provider Options

The application supports two LLM providers:

#### 1. OpenAI (Default)
You can select from various OpenAI models:
- `gpt-4o-mini` (default, cost-effective)
- `gpt-4o` (latest GPT-4 optimized)
- `gpt-4-turbo` (fast GPT-4)
- `gpt-3.5-turbo` (fastest, most economical)

Configuration via UI sidebar or `.env` file.

#### 2. Azure OpenAI
To use Azure OpenAI, you need:
- **API Key**: Your Azure OpenAI service key
- **Endpoint**: Your Azure OpenAI resource endpoint (e.g., `https://your-resource.openai.azure.com/`)
- **Deployment Name**: The name of your deployed model (e.g., `gpt-4`, `gpt-35-turbo`)
- **API Version**: The API version to use (default: `2024-02-15-preview`)

**How to get Azure OpenAI credentials:**
1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your Azure OpenAI resource
3. Under "Keys and Endpoint", copy:
   - One of the keys (KEY 1 or KEY 2)
   - The endpoint URL
4. Under "Model deployments", note your deployment name

**Setting up Azure OpenAI:**
- In the sidebar: Select "Azure OpenAI" and fill in all fields
- Via `.env` file: Set `LLM_PROVIDER=azureopenai` and configure all Azure variables

## Project Structure

```
crew-ai/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .env                  # Your actual API keys (not tracked in git)
└── README.md             # This file
```

## How It Works

1. **User Input**: You enter a query in the Streamlit interface

2. **Intent Classification**: The Intent Classifier Agent analyzes your query and categorizes it as:
   - **SUMMARY**: Requests for overviews or summaries
   - **COMPARE**: Requests to compare multiple items
   - **QNA**: Direct questions requiring specific answers

3. **Routing**: Based on the detected intent, the query is routed to the appropriate specialized agent

4. **Processing**: The specialized agent processes the query using its expertise

5. **Response**: The final answer is displayed in the UI

## Troubleshooting

### API Key Issues

**OpenAI:**
- Make sure your OpenAI API key is valid and has available credits
- Check that the key is properly set in the `.env` file or sidebar
- Verify you have access to the selected model

**Azure OpenAI:**
- Ensure all four fields are filled correctly (API Key, Endpoint, Deployment, API Version)
- Verify your endpoint URL format: `https://your-resource.openai.azure.com/` (with trailing slash)
- Check that your deployment name matches exactly what's in Azure Portal
- Ensure your Azure subscription has quota for the model
- Verify the API version is compatible with your deployment

### Installation Issues
- Ensure you're using Python 3.8 or higher
- Try creating a fresh virtual environment
- Update pip: `pip install --upgrade pip`

### Runtime Errors
- Check the console/terminal for detailed error messages
- Verify all dependencies are installed: `pip list`
- Ensure you have an active internet connection
- For Azure OpenAI errors, click "See error details" in the UI for more information

## Technologies Used

- **CrewAI**: Multi-agent orchestration framework
- **Streamlit**: Web application framework
- **OpenAI / Azure OpenAI**: LLM providers
- **Python**: Programming language

## License

This project is open source and available for educational and commercial use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Future Enhancements

- [ ] Add support for file uploads (PDFs, documents)
- [ ] Implement conversation history
- [ ] Add more specialized agents (research, coding, etc.)
- [ ] Support for custom agent configurations
- [ ] Integration with vector databases for RAG

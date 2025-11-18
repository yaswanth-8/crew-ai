# Project Structure Documentation

## Overview
This CrewAI application has been modularized into a clean, maintainable architecture with separated concerns.

## Directory Structure

```
crew-ai/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .env.example               # Example environment variables
├── README.md                  # Project documentation
├── STRUCTURE.md               # This file - structure documentation
└── src/                       # Source code directory
    ├── __init__.py
    ├── config/                # Configuration module
    │   ├── __init__.py
    │   └── llm_config.py     # LLM provider configuration
    ├── agents/                # Agent definitions
    │   ├── __init__.py
    │   ├── intent_classifier.py   # Intent classification agent
    │   ├── summary_agent.py       # Summary generation agent
    │   ├── compare_agent.py       # Comparison analysis agent
    │   └── qna_agent.py           # Question answering agent
    ├── tasks/                 # Task definitions
    │   ├── __init__.py
    │   ├── intent_tasks.py       # Intent classification task
    │   ├── summary_tasks.py      # Summary generation task
    │   ├── compare_tasks.py      # Comparison task
    │   └── qna_tasks.py          # Q&A task
    ├── crew/                  # Crew orchestration
    │   ├── __init__.py
    │   └── query_processor.py    # Main query processing logic
    ├── ui/                    # Streamlit UI components
    │   ├── __init__.py
    │   ├── sidebar.py            # Sidebar configuration UI
    │   ├── main_interface.py     # Main query interface
    │   └── result_display.py     # Results display components
    └── utils/                 # Utility functions
        ├── __init__.py
        └── constants.py          # Application constants
```

## Module Descriptions

### 1. **config/** - Configuration Module
- **llm_config.py**: Handles LLM initialization for both OpenAI and Azure OpenAI
  - `get_llm()`: Returns configured LLM instance
  - `validate_config()`: Validates provider configuration

### 2. **agents/** - Agent Definitions
Each agent is defined in its own file for clarity and maintainability:
- **intent_classifier.py**: Classifies user query intent (SUMMARY/COMPARE/QNA)
- **summary_agent.py**: Generates comprehensive summaries
- **compare_agent.py**: Provides detailed comparisons
- **qna_agent.py**: Answers specific questions

### 3. **tasks/** - Task Definitions
Task creation functions for each agent:
- **intent_tasks.py**: Creates intent classification task
- **summary_tasks.py**: Creates summary generation task
- **compare_tasks.py**: Creates comparison task
- **qna_tasks.py**: Creates Q&A task

### 4. **crew/** - Orchestration
- **query_processor.py**: `QueryProcessor` class that:
  - Initializes all agents
  - Creates tasks based on user query
  - Orchestrates the hierarchical crew workflow
  - Extracts and returns results

### 5. **ui/** - User Interface Components
Streamlit UI components separated by functionality:
- **sidebar.py**: Configuration sidebar (LLM provider settings)
- **main_interface.py**: Main query input interface
- **result_display.py**: Results and error display

### 6. **utils/** - Utilities
- **constants.py**: Application-wide constants (intent types, colors, etc.)

## Benefits of This Structure

### 1. **Separation of Concerns**
- Each module has a single, well-defined responsibility
- UI logic separated from business logic
- Agent definitions isolated from task definitions

### 2. **Maintainability**
- Easy to find and modify specific components
- Changes to one agent don't affect others
- Clear module boundaries

### 3. **Scalability**
- Easy to add new agents (create new file in `agents/`)
- Easy to add new tasks (create new file in `tasks/`)
- Easy to extend UI (add components to `ui/`)

### 4. **Testability**
- Each module can be tested independently
- Mock dependencies easily
- Clear interfaces between modules

### 5. **Reusability**
- Agents can be reused in different crews
- Tasks can be composed differently
- UI components can be reused

## How to Add New Features

### Adding a New Agent
1. Create `src/agents/new_agent.py`
2. Define `create_new_agent()` function
3. Export in `src/agents/__init__.py`
4. Use in `QueryProcessor`

### Adding a New Task
1. Create `src/tasks/new_task.py`
2. Define `create_new_task()` function
3. Export in `src/tasks/__init__.py`
4. Use in `QueryProcessor`

### Adding UI Components
1. Create component in `src/ui/new_component.py`
2. Export in `src/ui/__init__.py`
3. Use in `app.py`

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Environment Configuration

Copy `.env.example` to `.env` and configure your LLM provider:

```env
# For OpenAI
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini

# For Azure OpenAI
LLM_PROVIDER=azure
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

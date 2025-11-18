"""Sidebar UI components for configuration"""

import streamlit as st
import os


def render_sidebar():
    """
    Render the sidebar with LLM provider configuration

    Returns:
        None
    """
    with st.sidebar:
        st.header("Configuration")

        # Provider selection
        provider = st.selectbox(
            "Select LLM Provider",
            ["OpenAI", "Azure OpenAI"],
            index=0 if os.getenv("LLM_PROVIDER", "openai").lower() == "openai" else 1,
            help="Choose between OpenAI or Azure OpenAI"
        )

        # Set provider
        if "azure" in provider.lower():
            os.environ["LLM_PROVIDER"] = "azure"
        else:
            os.environ["LLM_PROVIDER"] = "openai"

        st.markdown("---")

        # Configuration based on provider
        if provider == "OpenAI":
            _render_openai_config()
        else:
            _render_azure_config()

        st.markdown("---")
        _render_example_queries()


def _render_openai_config():
    """Render OpenAI configuration fields"""
    st.subheader("OpenAI Settings")

    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Enter your OpenAI API key"
    )

    model = st.selectbox(
        "Model",
        ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
        index=0,
        help="Select the OpenAI model to use"
    )

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_MODEL"] = model
        st.success("OpenAI configured!")
    else:
        st.warning("Please enter your OpenAI API Key")


def _render_azure_config():
    """Render Azure OpenAI configuration fields"""
    st.subheader("Azure OpenAI Settings")

    azure_api_key = st.text_input(
        "Azure OpenAI API Key",
        type="password",
        value=os.getenv("AZURE_OPENAI_API_KEY", ""),
        help="Enter your Azure OpenAI API key"
    )

    azure_endpoint = st.text_input(
        "Azure OpenAI Endpoint",
        value=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
        help="Enter your Azure OpenAI endpoint (e.g., https://your-resource.openai.azure.com/)",
        placeholder="https://your-resource.openai.azure.com/"
    )

    azure_deployment = st.text_input(
        "Deployment Name",
        value=os.getenv("AZURE_OPENAI_DEPLOYMENT", ""),
        help="Enter your Azure OpenAI deployment name",
        placeholder="gpt-4"
    )

    azure_api_version = st.text_input(
        "API Version",
        value=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
        help="Enter the API version"
    )

    if azure_api_key and azure_endpoint and azure_deployment:
        os.environ["AZURE_OPENAI_API_KEY"] = azure_api_key
        os.environ["AZURE_OPENAI_ENDPOINT"] = azure_endpoint
        os.environ["AZURE_OPENAI_DEPLOYMENT"] = azure_deployment
        os.environ["AZURE_OPENAI_API_VERSION"] = azure_api_version
        st.success("Azure OpenAI configured!")
    else:
        st.warning("Please fill in all Azure OpenAI fields")


def _render_example_queries():
    """Render example queries section"""
    st.markdown("""
    ### Example Queries

    **Summary:**
    - "Summarize the benefits of AI"
    - "Give me an overview of machine learning"

    **Compare:**
    - "Compare Python and JavaScript"
    - "What are the differences between SQL and NoSQL?"

    **Q&A:**
    - "What is quantum computing?"
    - "How does blockchain work?"
    """)

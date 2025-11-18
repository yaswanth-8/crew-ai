"""
AI Query Assistant with CrewAI - Main Application
Modularized architecture with separate components for agents, tasks, UI, and configuration
"""

import streamlit as st
from dotenv import load_dotenv

from src.config import validate_config
from src.ui import render_sidebar, render_main_interface, display_results, display_error
from src.crew import QueryProcessor

# Load environment variables from .env file
load_dotenv()


def main():
    """Main application entry point"""
    # Page configuration
    st.set_page_config(
        page_title="AI Query Assistant",
        page_icon="",
        layout="wide"
    )

    # Render sidebar for configuration
    render_sidebar()

    # Render main interface
    user_query, submit_button, clear_button = render_main_interface()

    # Handle clear button
    if clear_button:
        st.rerun()

    # Handle submit button
    if submit_button and user_query:
        # Validate configuration
        is_valid, error_msg = validate_config()

        if not is_valid:
            st.error(f"{error_msg}")
        else:
            with st.spinner("Analyzing your query and generating response..."):
                try:
                    # Initialize query processor
                    processor = QueryProcessor()

                    # Process the query
                    intent, answer = processor.process(user_query)

                    # Display results
                    display_results(intent, answer)

                except Exception as e:
                    display_error(str(e))


if __name__ == "__main__":
    main()

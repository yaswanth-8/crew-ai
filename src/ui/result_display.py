"""Result display UI components"""

import streamlit as st


def display_results(intent, answer):
    """
    Display the query results

    Args:
        intent: The detected intent (SUMMARY, COMPARE, or QNA)
        answer: The answer from the agent

    Returns:
        None
    """
    st.success("Query processed successfully!")

    # Display intent with color coding
    intent_colors = {
        "SUMMARY": "",
        "COMPARE": "",
        "QNA": ""
    }
    st.markdown(f"### Detected Intent: {intent_colors.get(intent, '')} {intent}")

    # Display answer
    st.markdown("### Response:")
    st.markdown(answer)


def display_error(error_message):
    """
    Display error message

    Args:
        error_message: The error message to display

    Returns:
        None
    """
    st.error(f"An error occurred: {error_message}")
    st.info("Please check your configuration and try again.")
    with st.expander("See error details"):
        st.code(str(error_message))

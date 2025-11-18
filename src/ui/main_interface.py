"""Main interface UI components"""

import streamlit as st


def render_main_interface():
    """
    Render the main query interface

    Returns:
        tuple: (user_query, submit_clicked, clear_clicked)
    """
    st.title("AI Query Assistant with CrewAI")
    st.markdown("""
    This intelligent assistant uses CrewAI to:
    1. **Identify** your query intent (Summary, Compare, or Q&A)
    2. **Route** it to the appropriate specialized agent
    3. **Provide** a comprehensive response
    """)

    # Main query input
    user_query = st.text_area(
        "Enter your query:",
        height=100,
        placeholder="Ask me anything! I'll identify if you want a summary, comparison, or answer..."
    )

    # Buttons
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        submit_button = st.button("Submit", type="primary", use_container_width=True)
    with col2:
        clear_button = st.button("Clear", use_container_width=True)

    return user_query, submit_button, clear_button

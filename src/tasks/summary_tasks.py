"""Summary Task"""

from crewai import Task


def create_summary_task(user_query, summary_agent):
    """
    Create a task to provide a summary

    Args:
        user_query: The user's input query
        summary_agent: The summary agent

    Returns:
        Task: Summary task
    """
    return Task(
        description=f"""Provide a clear and concise summary for the following query:

        {user_query}

        Create a well-structured summary that captures the key points and essential information.
        Only execute this task if the intent is SUMMARY.""",
        agent=summary_agent,
        expected_output="A comprehensive summary addressing the query"
    )

"""Comparison Task"""

from crewai import Task


def create_compare_task(user_query, compare_agent):
    """
    Create a task to provide a comparison

    Args:
        user_query: The user's input query
        compare_agent: The compare agent

    Returns:
        Task: Comparison task
    """
    return Task(
        description=f"""Provide a detailed comparison for the following query:

        {user_query}

        Include:
        - Key similarities
        - Key differences
        - Advantages and disadvantages
        - A clear conclusion or recommendation if appropriate
        Only execute this task if the intent is COMPARE.""",
        agent=compare_agent,
        expected_output="A structured comparison addressing the query"
    )

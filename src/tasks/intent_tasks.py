"""Intent Classification Task"""

from crewai import Task


def create_intent_task(user_query, intent_classifier):
    """
    Create a task to classify the intent of user query

    Args:
        user_query: The user's input query
        intent_classifier: The intent classifier agent

    Returns:
        Task: Intent classification task
    """
    return Task(
        description=f"""Analyze the following user query and classify its intent.

        User Query: {user_query}

        Respond with ONLY one of these three words: SUMMARY, COMPARE, or QNA

        Guidelines:
        - SUMMARY: If the query asks for an overview, summary, or brief explanation
        - COMPARE: If the query asks to compare, contrast, or analyze differences/similarities
        - QNA: If the query asks a specific question requiring a direct answer
        """,
        agent=intent_classifier,
        expected_output="One word: SUMMARY, COMPARE, or QNA"
    )

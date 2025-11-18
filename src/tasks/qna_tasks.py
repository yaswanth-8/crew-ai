"""Question and Answer Task"""

from crewai import Task


def create_qna_task(user_query, qna_agent):
    """
    Create a task to answer a question

    Args:
        user_query: The user's input query
        qna_agent: The QnA agent

    Returns:
        Task: QnA task
    """
    return Task(
        description=f"""Answer the following question comprehensively:

        {user_query}

        Provide a detailed, accurate answer that directly addresses the question.
        Only execute this task if the intent is QNA.""",
        agent=qna_agent,
        expected_output="A comprehensive answer to the question"
    )

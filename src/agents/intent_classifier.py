"""Intent Classifier Agent - Classifies user query intent"""

from crewai import Agent
from src.config import get_llm


def create_intent_classifier():
    """Creates an agent that classifies the intent of user queries"""
    return Agent(
        role='Intent Classifier',
        goal='Accurately identify whether a user query is asking for a summary, comparison, or question/answer',
        backstory="""You are an expert at understanding user intent. You analyze queries and
        categorize them into three types:
        - SUMMARY: When users want a brief overview or summary of information
        - COMPARE: When users want to compare two or more items, concepts, or options
        - QNA: When users have specific questions that need direct answers

        You only respond with one of these three categories: SUMMARY, COMPARE, or QNA.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

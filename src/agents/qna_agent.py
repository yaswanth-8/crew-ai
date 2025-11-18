"""QnA Agent - Answers specific questions"""

from crewai import Agent
from src.config import get_llm


def create_qna_agent():
    """Creates an agent specialized in answering questions"""
    return Agent(
        role='Question Answering Expert',
        goal='Provide accurate, detailed, and helpful answers to specific questions',
        backstory="""You are an expert at answering questions with accuracy and clarity.
        You provide comprehensive answers that directly address the question, include relevant
        context when needed, and ensure the information is accurate and helpful.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

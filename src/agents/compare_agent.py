"""Compare Agent - Provides detailed comparisons"""

from crewai import Agent
from src.config import get_llm


def create_compare_agent():
    """Creates an agent specialized in comparisons"""
    return Agent(
        role='Comparison Analyst',
        goal='Provide detailed, objective comparisons between items, concepts, or options',
        backstory="""You are an expert at analyzing and comparing different items, concepts,
        or options. You identify similarities, differences, advantages, and disadvantages.
        You present comparisons in a structured format with clear criteria and objective analysis.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

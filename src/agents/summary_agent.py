"""Summary Agent - Provides comprehensive summaries"""

from crewai import Agent
from src.config import get_llm


def create_summary_agent():
    """Creates an agent specialized in providing summaries"""
    return Agent(
        role='Summary Specialist',
        goal='Provide clear, concise, and comprehensive summaries',
        backstory="""You are an expert at distilling complex information into clear,
        concise summaries. You identify key points, main ideas, and essential information
        while removing unnecessary details. You present information in a well-structured
        and easy-to-understand format.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

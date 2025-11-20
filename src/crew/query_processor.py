"""Query Processor - Orchestrates the crew workflow"""

from crewai import Crew, Process, Task
from src.agents import (
    create_intent_classifier,
    create_summary_agent,
    create_compare_agent,
    create_qna_agent
)
from src.config import get_llm


class QueryProcessor:
    """Handles query processing through the crew system"""

    def __init__(self):
        """Initialize the query processor"""
        self.intent_classifier = create_intent_classifier()
        self.summary_agent = create_summary_agent()
        self.compare_agent = create_compare_agent()
        self.qna_agent = create_qna_agent()

    def process(self, user_query):
        """
        Process user query through the crew system using hierarchical process

        Args:
            user_query: The user's input query

        Returns:
            tuple: (intent, answer)
        """
        # Create a single orchestration task without assigned agent
        orchestration_task = Task(
            description=f"""
            Process the following user query: '{user_query}'

            Follow these steps:
            1. First, use the Intent Classifier agent to determine the intent (SUMMARY, COMPARE, or QNA)
            2. Based on the detected intent, delegate to the appropriate specialized agent:
               - If SUMMARY: Delegate to Summary Specialist
               - If COMPARE: Delegate to Comparison Analyst
               - If QNA: Delegate to Question Answering Expert
            3. Return the final answer from the specialized agent

            Important: Only invoke ONE specialized agent based on the intent.
            """,
            expected_output="The answer from the appropriate specialized agent based on query intent",
            # No agent assigned - manager will orchestrate
        )

        # Create hierarchical crew with manager
        crew = Crew(
            agents=[
                self.intent_classifier,
                self.summary_agent,
                self.compare_agent,
                self.qna_agent
            ],
            tasks=[orchestration_task],
            process=Process.hierarchical,
            verbose=True,
            manager_llm=get_llm()
        )

        # Execute the crew workflow
        result = crew.kickoff()

        # Extract intent from results
        intent = self._extract_intent(result)

        return intent, result.raw

    def _extract_intent(self, result):
        """
        Extract the classified intent from crew results

        Args:
            result: The crew execution result

        Returns:
            str: The detected intent (SUMMARY, COMPARE, QNA, or UNKNOWN)
        """
        intent = "UNKNOWN"
        if hasattr(result, 'tasks_output') and len(result.tasks_output) > 0:
            intent_output = result.tasks_output[0].raw.strip().upper()
            if "SUMMARY" in intent_output:
                intent = "SUMMARY"
            elif "COMPARE" in intent_output:
                intent = "COMPARE"
            elif "QNA" in intent_output:
                intent = "QNA"

        return intent

from crewai.tools import BaseTool
import os

class FileReadTool(BaseTool):
    name: str = "Sport File Reader"
    description: str = "Reads the content of a file based on the sport name. Useful when you need to get information about cricket, football, or badminton to summarize it. Input should be the name of the sport or the query."

    def _run(self, query: str) -> str:
        query = query.lower().strip()
        valid_sports = ["cricket", "football", "badminton"]
        
        found_sport = None
        for sport in valid_sports:
            if sport in query:
                found_sport = sport
                break
        
        if found_sport:
            # Assuming the files are in the 'files' directory relative to the project root
            # We use absolute path for safety as we know the environment
            file_path = f"/Users/yaswanth/mydrive/genai-rnd/agents/crew-ai/files/{found_sport}.txt"
            try:
                with open(file_path, 'r') as f:
                    return f.read()
            except FileNotFoundError:
                return f"Error: File for {found_sport} not found at {file_path}."
        else:
            return "i cant summarize this, i can summarize only the avaible files (cricket, football, badminton)"

from langchain.tools import tool

@tool
def schedule_interviews(candidates: list, availability: dict) -> dict:
    """Schedules interviews based on candidate availability."""
    return {"schedule": "Next week: Mon-Wed, 2pm-4pm"}


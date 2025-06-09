from langchain.tools import tool

@tool
def search_candidates(jd: dict, filters: dict) -> list:
    """Searches mock candidates based on a JD and filter criteria."""
    return [
        {"name": "Alice", "skills": ["Python", "FastAPI"]},
        {"name": "Bob", "skills": ["LangChain", "LLM"]}
    ]


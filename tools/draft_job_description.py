from langchain_core.tools import Tool
from pydantic import BaseModel
from typing import List

# ✅ 1. Define args_schema using Pydantic
class JobDescriptionInput(BaseModel):
    role_title: str
    required_skills: List[str]
    budget: int

# ✅ 2. Define the actual function
def generate_job_description(role_title: str, required_skills: List[str], budget: int) -> str:
    return f"Drafting job description for '{role_title}' requiring {', '.join(required_skills)} within ${budget} budget."

# ✅ 3. Wrap it with Tool.from_function and pass args_schema
draft_job_description = Tool.from_function(
    func=generate_job_description,
    name="draft_job_description",
    description="Generates a job description from title, required skills, and budget.",
    args_schema=JobDescriptionInput
)

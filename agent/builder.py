from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent

from tools.draft_job_description import draft_job_description
from tools.search_candidates import search_candidates
from tools.estimate_costs import estimate_costs
from tools.schedule_interviews import schedule_interviews
from memory.in_memory import InMemoryStore
from config.config import OPENAI_API_KEY

def build_agent():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=OPENAI_API_KEY,
        streaming=True
    )

    tools = [
        draft_job_description,
        search_candidates,
        estimate_costs,
        schedule_interviews
    ]

    # ✅ Replaces initialize_agent — LangGraph prefers this tool-calling setup
    agent = create_tool_calling_agent(llm, tools)
    memory = InMemoryStore()  # optional if you use memory node in LangGraph
    return agent, memory

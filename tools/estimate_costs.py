from langchain.tools import tool

@tool
def estimate_costs(jd: dict, plan: dict) -> dict:
    """Estimates salary bands and recruitment costs."""
    return {
        "salary_band": "$120k-$150k",
        "recruiter_fee": "$15k",
        "tool_costs": "$2k"
    }

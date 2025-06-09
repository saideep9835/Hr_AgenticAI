from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from graph.hr_plan_graph import run_hr_graph
import traceback

app = FastAPI()

class PlanRequest(BaseModel):
    prompt: str  # User input description

class PlanResponse(BaseModel):
    plan: dict
    tool_trace: list

@app.post("/plan", response_model=PlanResponse)
async def generate_plan(request: PlanRequest):
    try:
        graph_state = run_hr_graph(request.prompt)

        # Extract final plan and build tool trace if needed
        final_plan = graph_state.get("result", {})
        steps = graph_state.get("step", None)

        # Optional: extract tool trace names based on your internal logic
        trace = []
        if steps:
            try:
                trace.append(steps.tool)  # if using structured steps
            except:
                trace.append("Unknown step")

        return {
            "plan": final_plan,
            "tool_trace": trace  # or hardcoded ["Job Description", "Candidate Search", ...]
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Plan generation failed: {str(e)}")




# /graph/hr_plan_graph.py

from langgraph.graph import END, StateGraph
from langchain_core.runnables import RunnableLambda
from agent.builder import build_agent

# Define LangGraph nodes
def planner_node(state):
    agent, _ = build_agent()
    next_action = agent.invoke(state["prompt"])
    state["step"] = next_action
    return state

def tool_runner_node(state):
    tool = state["step"].tool
    tool_input = state["step"].tool_input
    output = tool.invoke(tool_input)
    state["result"] = output
    return state

def memory_node(state):
    # Optionally store or update memory
    return state

def build_hr_plan_graph():
    builder = StateGraph()
    builder.add_node("Planner", RunnableLambda(planner_node))
    builder.add_node("ToolRunner", RunnableLambda(tool_runner_node))
    builder.add_node("Memory", RunnableLambda(memory_node))

    builder.set_entry_point("Planner")
    builder.add_edge("Planner", "ToolRunner")
    builder.add_edge("ToolRunner", "Memory")
    builder.add_edge("Memory", "Planner")

    # This checks if the planner's output signals we're done
    builder.add_conditional_edges("Planner", lambda x: END if x.get("step") == "FINISH" else None)

    return builder.compile()

def run_hr_graph(prompt: str):
    graph = build_hr_plan_graph()
    result = graph.invoke({"prompt": prompt})
    return result.get("result")


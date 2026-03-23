from langgraph.graph import StateGraph
from app.agent.state import AgentState
from app.agent.scout import scout_node
from app.agent.inspector import inspector_node
from app.agent.broker import broker_node
from app.agent.crm import crm_node

def build_graph():
    g = StateGraph(AgentState)

    g.add_node("scout", scout_node)
    g.add_node("inspector", inspector_node)
    g.add_node("broker", broker_node)
    g.add_node("crm", crm_node)

    g.set_entry_point("scout")

    g.add_edge("scout", "inspector")
    # g.add_edge("inspector", "broker")
    g.add_edge("broker", "crm")

    return g.compile()
from langgraph.graph import StateGraph
from app.agent.state import AgentState
from app.agent.scout import scout_node
from app.agent.broker import broker_node
from app.agent.crm import crm_node
from app.agent.filter import filter_node


def build_graph():
    g = StateGraph(AgentState)

    g.add_node("scout", scout_node)
    g.add_node("filter", filter_node)
    g.add_node("broker", broker_node)
    g.add_node("crm", crm_node)

    g.set_entry_point("scout")

    g.add_edge("scout", "filter")
    g.add_edge("filter", "broker")
    g.add_edge("broker", "crm")

    return g.compile()
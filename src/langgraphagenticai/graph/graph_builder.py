from langgraph.graph import StateGraph
from langgraph.graph import START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graph_builder = StateGraph(State)


    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using langgraph this methos
        initializes a chatbot node using the BasicChatbotNode class
        """
        self.basic_chatbot = BasicChatbotNode(self.model)

        self.graph_builder.add_node("chatbot", self.basic_chatbot.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()
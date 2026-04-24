from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    A Basic Chatbot login implementation
    """
    def __init__(self,model):
        self.model = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response
        """
        return {"messages": self.model.invoke(state["messages"])}
    
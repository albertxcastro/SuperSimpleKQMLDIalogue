class Message:
    def __init__(self, to_agent: str, from_agent: str, content: str):
        self.to_agent = to_agent
        self.from_agent = from_agent
        self.content = content

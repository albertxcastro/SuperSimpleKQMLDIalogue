import queue

from Agents.Agent import Agent
from Models.Message import Message


class Alice(Agent):
    def __init__(self, name: str, internal_queue: queue.Queue):
        super().__init__(name, internal_queue)

    def processMessage(self, message: Message):
        super().processMessage(message)
        trimmed = message.content[1: -1]  # remove parenthesis
        trimmed = trimmed.split(":content")

        request = trimmed[1]
        request = request[2: -1] # remove parenthesis
        params = request.split(' ')

        return f"{self.name}: Received response from {message.from_agent}. {params[0]} is {params[1]}"

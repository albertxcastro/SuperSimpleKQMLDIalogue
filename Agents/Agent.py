import queue

from Models.Message import Message


class Agent:
    def __init__(self, name: str, internal_queue: queue.Queue):
        self.name = name
        self.internal_queue = internal_queue

    def sendMessage(self, message: Message):
        self.internal_queue.put(message)

    def pollMessage(self):
        if self.internal_queue.empty():
            print(f"Agent {self.name} attempted to read a message but the queue was empty")
            return

        message: Message = self.internal_queue.get()
        return self.processMessage(message)

    def processMessage(self, message: Message):
        print(f"{self.name}: Received a mesage from {message.from_agent}. Content: {message.content}")




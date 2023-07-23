import queue

from Agents.Agent import Agent
from Models.Message import Message


class Bob(Agent):
    def __init__(self, name: str, internal_queue: queue.Queue):
        super().__init__(name, internal_queue)
        self.prev_request = {}
        self.knowledgeBase = {}

    def setKnowledgeBaseItem(self, item, value):
        self.knowledgeBase[item] = value

    def processMessage(self, message: Message):
        super().processMessage(message)
        trimmedParams = message.content[1: -1].split(' ')  # remove parenthesis
        main_param = trimmedParams[-1]  # this can be television or HDMI_slots

        message_to = ""

        if main_param == "television":
            size = int(trimmedParams[1])
            available_stock = sum(1 for tv in self.knowledgeBase.values() if tv.inch_size == size)
            content = f"(tell :content ({trimmedParams[0]} {available_stock}))"

            return_message = Message("alice", self.name, content)
            self.internal_queue.put(return_message)

            self.prev_request = {"inch_size": size}
            message_to = return_message.to_agent

        elif main_param == "HDMI_slots":
            prev_inch_size_request = self.prev_request["inch_size"]
            for tv in self.knowledgeBase.values():
                if tv.inch_size == prev_inch_size_request:
                    hdmi_available_stock = tv.hdmi_slots
                    content = f"(tell :content (available_stock {hdmi_available_stock}))"
                    return_message = Message("alice", self.name, content)
                    self.internal_queue.put(return_message)
                    message_to = return_message.to_agent
                    break

        return f"{self.name}: Message processed. Put a response in the queue to {message_to}. Content: {message.content}"

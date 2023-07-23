import queue

from Agents.Alice import Alice
from Agents.Bob import Bob
from Models.Message import Message
from Models.Television import Television

communicationQueue = queue.Queue()

# initialize alice and bob
alice = Alice("alice", communicationQueue)
bob = Bob("bob", communicationQueue)

# backfill Bob's knowledge base about TVs
bob.setKnowledgeBaseItem("Television1", Television(50, 3))
bob.setKnowledgeBaseItem("Television2", Television(50, 3))
bob.setKnowledgeBaseItem("Television3", Television(50, 3))
bob.setKnowledgeBaseItem("Television4", Television(50, 3))
bob.setKnowledgeBaseItem("Television5", Television(50, 3))
bob.setKnowledgeBaseItem("Television6", Television(50, 3))
bob.setKnowledgeBaseItem("Television7", Television(50, 3))
bob.setKnowledgeBaseItem("Television8", Television(50, 3))
bob.setKnowledgeBaseItem("Television9", Television(32, 1))
bob.setKnowledgeBaseItem("Television0", Television(42, 1))

# alice asks bob about 50 inch TVs
message = Message("bob", alice.name, "(available_stock 50 inch television)")
alice.sendMessage(message)

# bob receives alice's request and put a response in the message queue
response = bob.pollMessage()
print(response)

# alice receives bob's reponse
response = alice.pollMessage()
print(response)

# send another ask message to bob
message = Message("bob", alice.name, "(available_stock HDMI_slots)")
alice.sendMessage(message)

response = bob.pollMessage()
print(response)

response = alice.pollMessage()
print(response)

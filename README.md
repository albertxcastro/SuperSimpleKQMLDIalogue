## Activity Guidance
Create an agent dialogue, using KQML and KIF, between two agents (named Alice and Bob).

Alice is an agent designed to procure stock and Bob is an agent that controls the stock levels for a warehouse. This dialogue should see Alice asking Bob about the available stock of 50 inch televisions, and also querying the number of HDMI slots the televisions have.

Add your completed answers to your e-Portfolio.

## Learning Outcomes
An understanding of the motivations for, and appropriate use of, agent-based computing.
An understanding of the main agent models in use today and their grounding in artificial intelligence research.

### How to run
Open a terminal and navigate to the root of the project, then type:
```
python main.py
```
and hit enter.

You should see the following output:
```
(venv) (base) albertxcastro@Albertos-MacBook-Pro SimpleAgentDialogue % python main.py 
bob: Received a mesage from alice. Content: (available_stock 50 inch television)
bob: Message processed. Put a response in the queue to alice. Content: (available_stock 50 inch television)
alice: Received a mesage from bob. Content: (tell :content (available_stock 8))
alice: Received response from bob. available_stock is 8
bob: Received a mesage from alice. Content: (available_stock HDMI_slots)
bob: Message processed. Put a response in the queue to alice. Content: (available_stock HDMI_slots)
alice: Received a mesage from bob. Content: (tell :content (available_stock 3))
alice: Received response from bob. available_stock is 3
(venv) (base) albertxcastro@Albertos-MacBook-Pro SimpleAgentDialogue % 
```

### Project files
```
├── Agents
│   ├── Agent.py
│   ├── Alice.py
│   └── Bob.py
├── Models
│   ├── Message.py
│   └── Television.py
├── main.py
```

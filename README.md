# First-multi-agent system with google-adk
## Google ADK Agent

### System Diagram

Below is a high-level system diagram showing the agent architecture and flow:

```
+-----------------------------+
|         root_agent          |  (agent.py)
|-----------------------------|
| LlmAgent                    |
| - Coordinates flow          |
| - Delegates to subagents    |
| - Subagent: chat_agent      |
+-------------+---------------+
              |
              v
+-----------------------------+
|         chat_agent          |  (subagent/chat/agent.py)
|-----------------------------|
| LlmAgent                    |
| - Handles student queries   |
| - Delegates resource reqs   |
| - Subagent: resources_agent |
+-------------+---------------+
              |
              v
+-----------------------------+
|       resources_agent       |  (subagent/resources/agent.py)
|-----------------------------|
| Agent                       |
| - Finds online resources    |
| - Uses RESOURCE_AGENT_INST. |
| - Tool: google_search_grounding
+-------------+---------------+
              |
              v
+-----------------------------+
|   google_search_grounding   |  (tools/search.py)
|-----------------------------|
| AgentTool                   |
| - Wraps google_search tool  |
| - Custom search prompt      |
+-----------------------------+
```

### Set Up Environment & Install ADK

#### Create Virtual Environment
```bash
python -m venv .venv
```

#### Activate Virtual Environment (Run in each new terminal)
- **macOS/Linux**: 
    ```bash
    source .venv/bin/activate
    ```
- **Windows CMD**: 
    ```cmd
    .venv\Scripts\activate.bat
    ```
- **Windows PowerShell**: 
    ```powershell
    .venv\Scripts\Activate.ps1
    ```

#### Install ADK
```bash
pip install google-adk -q
```

### Set up the model
- Create .env file under student_multi_agent_system and add the below content replacing your API key.
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

### To run the agents
- go to root path /student_multi_agent_system
```
adk web
```


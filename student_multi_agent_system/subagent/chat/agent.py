"""Chat Agent in a student support system that provides answers and delegates subagents."""
from google.adk.agents import LlmAgent
from dotenv import load_dotenv
from . import prompt
from student_multi_agent_system.subagent.resources.agent import resources_agent

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

chat_agent = LlmAgent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="chat_agent",
    description="A chat agent that responds to user queries by coordinating with specialized subagents for various tasks in a student support system.",
    instruction=prompt.CHAT_AGENT_PROMPT,
    sub_agents=[resources_agent]
)
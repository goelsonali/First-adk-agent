"""Resource Agent in a student support system that searches Google for relevant resources."""

from google.adk.agents import Agent
from . import prompt
from student_multi_agent_system.tools.search import google_search_grounding

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"


resources_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="resources_agent",
    description="Given some text, search Google for the most relevant, trustworthy, and helpful online resources (such as articles, guides, or tools) in response to the user's query.",
    instruction=prompt.RESOURCE_AGENT_INSTRUCTION,
    tools=[google_search_grounding]
)
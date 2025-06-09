"""Resource Agent in a mental wellness support system that searches Google for relevant resources."""

import os
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from multi_tool_agent.shared_libraries.types import ResourceSearchResponse,json_response_config
from . import prompt
from dotenv import load_dotenv
from multi_tool_agent.tools.search import google_search_grounding
from multi_tool_agent.shared_libraries.types import ResourceSearchResponse,json_response_config

load_dotenv()

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"


resources_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="resources_agent",
    description="Given an itinerary, this agent keeps up to date and provides relevant travel information to the user before the trip.",
    instruction=prompt.RESOURCE_AGENT_INSTRUCTION,
    tools=[google_search_grounding]
)
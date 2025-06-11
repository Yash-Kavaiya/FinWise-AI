from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

execution_analyst_agent = Agent(
    model=MODEL,
    name="execution_analyst_agent",
    instruction=prompt.EXECUTION_ANALYST_PROMPT,
    output_key="execution_plan_output",
)
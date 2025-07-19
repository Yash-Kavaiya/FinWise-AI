from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

risk_analyst_agent = Agent(
    model=MODEL,
    name="risk_analyst_agent",
    instruction=prompt.RISK_ANALYST_PROMPT,
    output_key="risk_analysis_output",
)
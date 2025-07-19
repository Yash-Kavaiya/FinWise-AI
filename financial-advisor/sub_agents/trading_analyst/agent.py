from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

trading_analyst_agent = Agent(
    model=MODEL,
    name="trading_analyst_agent",
    instruction=prompt.TRADING_ANALYST_PROMPT,
    output_key="trading_strategy_output",
)
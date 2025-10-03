from crewai import Task
from agents1 import marketing_agent

marketing_task=Task(
    description="Generate a 30-day marketing plan and ad copy for a product",
    agent=marketing_agent,
    expected_output="A structured plan with ad copy"
)
from crewai import Task
from agents1 import Health_agent

Health_task=Task(
    description="give good suggestion in the field of Health and what user will give the input based that give the suggestions",
    agent=Health_agent,
    expected_output="A structured plan with understander manner and in point wished manner"
)

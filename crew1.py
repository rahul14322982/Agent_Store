from crewai import Crew

from agents1 import Health_agent
from tasks1 import Health_task

crew=Crew(
    agents=[Health_agent],
    tasks=[Health_task],
    verbose=True
)

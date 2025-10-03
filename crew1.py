from crewai import Crew

from agents1 import marketing_agent
from tasks1 import marketing_task

crew=Crew(
    agents=[marketing_agent],
    tasks=[marketing_task],
    verbose=True
)
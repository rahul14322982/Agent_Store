from crewai import Agent
#import os
from dotenv import load_dotenv
load_dotenv()
from crewai import LLM

llm=LLM(
    #provider="openai",
    #api_key=os.getenv("OPENAI_API_KEY"),
    model="gemini/gemini-2.0-flash",
    temperature=0.2,
)

Health_agent=Agent(
    role="Health care Expert",
    goal="Give the tips to containing the good health",
    backstory="Experienced in the giving tips to health care",
    llm=llm,

    verbose=True
)


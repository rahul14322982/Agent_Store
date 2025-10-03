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

marketing_agent=Agent(
    role="Marketing Expert",
    goal="Create marketing plans & ad copy",
    backstory="Experienced marketer with SEO and social campaigns",
    llm=llm,

    verbose=True
)


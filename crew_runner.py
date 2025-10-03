#from django.db.models.expressions import result

from agents1 import marketing_agent

def run_marketing_agent(inputs1:dict):
    #import os
    #os.environ["OPENAI_API_KEY"] = api_key
    return marketing_agent.kickoff(inputs1)
#from django.db.models.expressions import result

from agents1 import Health_agent

def run_health_agent(inputs1:dict):

    return Health_agent.kickoff(inputs1)

from fastapi import FastAPI
from api_agents import router as agent_router

app = FastAPI(titel="Agent health-Demo")
app.include_router(agent_router, prefix="/agents", tags=["agents"])

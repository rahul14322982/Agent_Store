from fastapi import FastAPI
from api_agents import router as agent_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(titel="Agent health-Demo")
app.include_router(agent_router, prefix="/agents", tags=["agents"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

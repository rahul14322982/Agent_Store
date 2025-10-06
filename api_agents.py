from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from crew_runner import run_health_agent as run_health_logic
from typing import Any

router=APIRouter()

class RunRequest(BaseModel):
    inputs1:list[dict[str, Any]]
    #api_key:str

@router.post("/agents1/health/run")
def run_health_agent(req:RunRequest):
    try:
        result = run_health_logic(req.inputs1)
        return {"result":result}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

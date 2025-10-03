from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from crew_runner import run_marketing_agent as run_marketing_logic
from typing import Any

router=APIRouter()

class RunRequest(BaseModel):
    inputs1:list[dict[str, Any]]
    #api_key:str

@router.post("/agents1/marketing/run")
def run_marketing_agent(req:RunRequest):
    try:
        result = run_marketing_logic(req.inputs1)
        return {"result":result}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
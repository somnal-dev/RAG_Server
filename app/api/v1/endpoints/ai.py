from fastapi import APIRouter

from app.core.agent import agent
from app.model.ai import PromptRequest

router = APIRouter(prefix="/api/ai", tags=["ai"])

@router.get("/")
def default():
    return {
        "message": "API Router"
    }

@router.post("/prompt")
def prompt(request: PromptRequest):
    return agent.prompt(message = request.message)
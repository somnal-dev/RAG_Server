from fastapi import APIRouter

router = APIRouter(prefix="/api/ai", tags=["ai"])

@router.get("/")
def default():
    return {
        "message": "API Router"
    }
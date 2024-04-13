from fastapi.routing import APIRouter
from status import Status

api_router = APIRouter(prefix="/api")
status = Status()

@api_router.get("/status")
async def status():
    if status.online:
        return {"status": True}
    else:
        return {"status": False}


@api_router.get("/status/(test_a)")
async def status_testa(test_a: int):
    return {"testa": test_a * 2}

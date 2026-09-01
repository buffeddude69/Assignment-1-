from app.services import task_service
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_root():
    return task_service.get_root()

@router.get("/health")
async def get_health():
    return task_service.get_health()
# sample_database = {}

# @router.get("/tasks/{task_id}")
# async def get_task(task_id : int):
#     return task_service.get_task(task_id)
    
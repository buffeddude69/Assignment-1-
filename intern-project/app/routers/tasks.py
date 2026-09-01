from app.services import task_service
from fastapi import APIRouter

router = APIRouter()

sample_database = {}

@router.get("/")
async def get_root():
    return task_service.get_root()

@router.get("/health")
async def get_health():
    return task_service.get_health()

@router.get("/tasks")
async def get_tasks():
    return task_service.get_tasks()

@router.get("/tasks/{task_id}")
async def get_task(task_id : int):
    return task_service.get_task(task_id)
    
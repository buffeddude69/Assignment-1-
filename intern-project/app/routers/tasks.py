from app.services import task_service
from fastapi import APIRouter
from app.schemas.task import CreateTask, UpdateTask
from fastapi.responses import JSONResponse

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

@router.post("/tasks/{task_id}", status_code = 201)
async def create_task(task_id : int, task : CreateTask):
    return task_service.create_task(task_id, task)

@router.put("/tasks/{task_id}", status_code = 201)
async def update_task(task_id : int, task : UpdateTask):
    return task_service.update_task(task_id, task)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id : int):
    return task_service.delete_task(task_id)
    
from app.schemas.task import CreateTask
from fastapi.responses import JSONResponse

sample_db = {
    1: {
        "title": "Learn FastAPI",
        "description": "Learn layered architecture"
    }
}

def get_root():
    return {
        "name" : "Task API",
        "version" : "1.0",
        "endpoints" : ["/tasks"]
    }

def get_health():
    return {
        "status" : "ok"
    }

def get_tasks():
    return list(sample_db.values())

def get_task(task_id):
    if task_id in sample_db:
        return {"status" : "Found!", "task" : sample_db[task_id]}
    else:
        return JSONResponse(
            status_code=404,
            content={"error" : f"Task {task_id} not found"}
        )


    
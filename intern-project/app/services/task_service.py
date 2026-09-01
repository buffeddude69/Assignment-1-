from app.schemas.task import CreateTask
from fastapi.responses import JSONResponse
from fastapi import HTTPException   

sample_db = {
    1: {
        "title": "Learn FastAPI",
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

def create_task(task_id : int , task : CreateTask):

    if task_id in sample_db:
        raise HTTPException(
            status_code = 400,
            detail=f"Task {task_id} already exists"
        )
    
    sample_db[task_id] = task.model_dump()
    
    return {"status" : "Done! Here's your receipt", "task" : sample_db[task_id]}



    
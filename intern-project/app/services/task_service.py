from app.schemas.task import CreateTask


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
# sample_db = {
#     1: {
#         "name": "Task API",
#         "version": "1.0",
#         "endpoints": ["/tasks"]
#     }
# }

# def get_task(task_id):
#     if task_id in sample_db:
#         return {"status" : "Found!", "task" : sample_db[task_id]}
#     else:
#         return {"Error!" : "Task Not Found!"}


    
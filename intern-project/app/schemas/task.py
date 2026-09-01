from pydantic import BaseModel

class CreateTask(BaseModel):
    title : str

class UpdateTask(BaseModel):
    title : str
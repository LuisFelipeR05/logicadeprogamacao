from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    description: str
    priority: str
    category: str
    completed: bool = False
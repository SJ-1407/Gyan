from pydantic import BaseModel
from typing import List

class TaskBase(BaseModel):
    """
    Base class for task attributes.

    Attributes:
        title (str): The title of the task. It is required
        description (Optional[str]): The description of the task (optional).
        completed (bool): Indicates whether the task is completed.
    """
    title: str
    description: str | None = None
    completed:bool =False


class TaskCreate(TaskBase):
    """
    Represents the data required to create a new task.

    Inherits:
        TaskBase
    """
    pass

class TaskUpdate(TaskBase):
    """
    Represents the data required to update an existing task.

    Inherits:
        TaskBase
    """
    pass




class Task(TaskBase):
    """
    Represents a task with its attributes and an additional ID.

    Inherits:
        TaskBase

    Attributes:
        id (int): The unique identifier of the task.
    """
    id: int
    class Config:
        """
        Pydantic configuration for ORM mode.
        """
        orm_mode = True

class TaskList(BaseModel):
    """
    Represents a list of tasks.

    Attributes:
        tasks (List[Task]): List of tasks.
    """
    tasks: List[Task]



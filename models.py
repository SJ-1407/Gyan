from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Task(Base):
    """
    Represents a task model in the SQL database.

    Inherits:
        Base

    Attributes:
        id (Column): The unique identifier of the task.It is auto generated
        title (Column): The title of the task.
        description (Column): The description of the task.
        completed (Column): Indicates whether the task is completed.
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)

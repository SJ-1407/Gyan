from sqlalchemy.orm import Session
import models, schema
from typing import List

def read_task(db: Session, task_id: int):
    """
    Retrieve details of a specific task by ID mentioned by the client.

    Args:
        db (Session): The database session.
        task_id (int): The ID of the task to retrieve.

    Returns:
        models.Task: The details of the requested task.
    """
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: schema.TaskCreate):
    """
    Create a new task.

    Args:
        db (Session): The database session.
        task (schemas.TaskCreate): The details of the task to be created.

    Returns:
        models.Task: The newly created task.
    """
    db_task = models.Task(title=task.title,description=task.description,completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session,task_id:int, task: schema.TaskUpdate):
    """
    Update details of an existing task.

    Args:
        db (Session): The database session.
        task_id (int): The ID of the task to update.
        task (schemas.TaskUpdate): The updated details of the task.

    Returns:
        models.Task: The updated task.
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)   
        
        return db_task
    else: 
        return None
        
   

def delete_task(db: Session, task_id: int):
    """
    Delete a task by ID.

    Args:
        db (Session): The database session.
        task_id (int): The ID of the task to delete.

    Returns:
        bool: True if the task is deleted successfully, False otherwise.
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
     return False
       
    
    db.delete(db_task)
    db.commit()
    task = db_task
    return True

def read_all_tasks(db: Session, completed: bool|None = None) -> List[models.Task]:
    """
    Retrieve a list of all tasks, optionally filtered by completion status.

    Args:
        db (Session): The database session.
        completed (Optional[bool]): Filter tasks by completion status. Defaults to None.

    Returns:
        List[models.Task]: List of tasks.
    """
    if completed is not None:
        return db.query(models.Task).filter(models.Task.completed == completed).all()
    return db.query(models.Task).all()
   
   



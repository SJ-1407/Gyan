from fastapi import Depends, FastAPI, HTTPException,status,Query
from sqlalchemy.orm import Session

import crud, models,schema
from database import SessionLocal, engine
from typing import Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """
    Get a database session.

    Returns:
        sqlalchemy.orm.Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks/", response_model=schema.Task)
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.

    Args:
        task (schemas.TaskCreate): The details of the task to be created.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        schema.Task: The newly created task.
    """
    return crud.create_task(db, task)

@app.get("/tasks/{task_id}", response_model=schema.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Read the details of a specific task.

    Args:
        task_id (int): The ID of the task to retrieve.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        schema.Task: The details of the requested task.
    
    Raises:
        HTTPException: If the task with the given ID is not found (HTTP 404 Not Found).
    """
    db_task = crud.read_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schema.Task)
def update_task(task_id: int, task: schema.TaskUpdate, db: Session = Depends(get_db)):
    """
    Update details of an existing task.

    Args:
        task_id (int): The ID of the task to update.
        task (schema.TaskUpdate): The updated details of the task.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        schema.Task: The updated task.

    Raises:
        HTTPException: If the task with the given ID is not found (HTTP 404 Not Found).
    """
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by ID.

    Args:
        task_id (int): The ID of the task to delete.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary with a message indicating successful deletion.

    Raises:
        HTTPException: If the task with the given ID is not found (HTTP 404 Not Found).
    """
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.get("/tasks/", response_model=schema.TaskList)
def read_all_tasks(completed: Optional[bool] = Query(None, description="Filter tasks by completion status"), db: Session = Depends(get_db)):
    """
    Retrieve a list of all tasks, optionally filtered by completion status.

    Args:
        completed (Optional[bool]): Filter tasks by completion status. Defaults to None.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the list of tasks.

    Note:
        The list of tasks is wrapped in a dictionary to comply with the response_model.

    Examples:
        To get all tasks: `/tasks/`
        To filter tasks by completion status: `/tasks/?completed=true` or `/tasks/?completed=false`
    """
    tasks = crud.read_all_tasks(db, completed= completed)
    return {"tasks": tasks}




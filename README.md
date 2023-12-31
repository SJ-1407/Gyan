This project performs the CRUD operatioons using FastAPI


## Features
- Create a new task
- Retrieve a task by ID
- Update the details of an existing task
- Delete a task by ID
- Retrieve all tasks
- Retrieve tasks by completed status


## Prerequisites
- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Setup

1.Clone the repository:

    git clone -b master https://github.com/SJ-1407/GyanBee-Task.git  
    cd GyanBee-Task  
   
2.Create and activate a virtual environment:  

     python -m venv any_name     
     .\any_name\Scripts\activate   
  
3. Install dependencies:   

       pip install -r requirements.txt
   if the above command does not work , try:

       python -m uvicorn main:app --reload


5.  Run the app:    

        uvicorn main:app --reload

7. Make sure to change the database url present in database.py, if required.

 
#You can test the endpoints at http://127.0.0.1:8000/docs.

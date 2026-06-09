from fastapi import FastAPI
from task_service import *
from storage import load_tasks,save_tasks

app = FastAPI()

# Load existing tasks into service layer
tasks = load_tasks()


@app.post("/tasks/add")
def api_add_task(task: str):
    tasks = load_tasks()
    add_task(tasks,task)
    save_tasks(tasks)
    return {"message": "Task added", "tasks": tasks}


@app.get("/tasks")
def api_view_tasks():
    tasks = load_tasks()
    return {"tasks": view_tasks(tasks)}


@app.post("/tasks/complete")
def api_complete_task(index: int):
    tasks = load_tasks()
    complete_task(tasks, index)
    save_tasks(tasks)
    return {"message": "Task completed", "tasks": tasks}


@app.delete("/tasks/delete")
def api_delete_task(index: int):
    tasks = load_tasks()
    delete_task(tasks, index)
    save_tasks(tasks)
    return {"message": "Task deleted", "tasks": tasks}
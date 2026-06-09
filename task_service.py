from storage import save_tasks


def add_task(tasks, task):
    if not task.strip():
        return {"error": "Task cannot be empty"}

    tasks.append({
        "name": task,
        "done": False
    })

    save_tasks(tasks)
    return tasks


def view_tasks(tasks):
    return tasks


def complete_task(tasks, ind):
    if ind < 1 or ind > len(tasks):
        return {"error": "Invalid index"}

    if tasks[ind - 1]["done"]:
        return {"message": "Already completed"}

    tasks[ind - 1]["done"] = True
    save_tasks(tasks)
    return {"message": "Task completed"}


def delete_task(tasks, ind):
    if ind < 1 or ind > len(tasks):
        return {"error": "Invalid index"}

    removed = tasks.pop(ind - 1)
    save_tasks(tasks)
    return {"message": f"Deleted {removed['name']}"}
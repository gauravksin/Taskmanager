import json
import os

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            content = f.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        print("Warning: tasks.json corrupted. Resetting file.")
        return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)
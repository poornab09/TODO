import json
from models.task import Task
from utils.helper import is_overdue

FILE_PATH = "data/tasks.json"

def load_tasks():
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return [Task.from_dict(t) for t in data]
    except:
        return []

def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

def add_task(title, priority, deadline):
    tasks = load_tasks()
    tasks.append(Task(title, priority, deadline))
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "✔" if task.completed else "✘"
        overdue = "⚠️" if is_overdue(task.deadline) else ""
        print(f"{i+1}. {task.title} [{task.priority}] {status} {overdue}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        save_tasks(tasks)
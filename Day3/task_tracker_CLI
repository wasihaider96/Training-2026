import json
import sys
from datetime import datetime

# ------------------ Task Class ------------------
class Task:
    def __init__(self, id, title, status="todo", created_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at
        }

# ------------------ Task Manager ------------------
class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Error: JSON file is corrupt")
            self.tasks = []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        new_id = 1 if not self.tasks else self.tasks[-1].id + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added!")

    def list_tasks(self, filter_status=None):
        for task in self.tasks:
            if filter_status and task.status != filter_status:
                continue
            print(f"{task.id} | {task.title} | {task.status} | {task.created_at}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "done"
                self.save_tasks()
                print("Task marked as done!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted!")
                return
        print("Task not found!")


# ------------------ CLI ------------------
manager = TaskManager()

if len(sys.argv) < 2:
    print("Usage: python tasks.py [add|list|done|delete]")
    sys.exit()

command = sys.argv[1]

if command == "add":
    title = " ".join(sys.argv[2:])
    manager.add_task(title)

elif command == "list":
    if len(sys.argv) > 2:
        manager.list_tasks(sys.argv[2])
    else:
        manager.list_tasks()

elif command == "done":
    manager.complete_task(int(sys.argv[2]))

elif command == "delete":
    manager.delete_task(int(sys.argv[2]))

else:
    print("Unknown command")
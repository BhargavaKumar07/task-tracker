import os
import json
from datetime import datetime
import sys
TASK_FILE = "tasks.json"

def initialize_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file, indent=4)

def load_tasks():
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "created_at": current_time,
        "updated_at": current_time
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"task added Successfully: {new_id}")
    
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created At: {task['created_at']}")
        print(f"Updated At: {task['updated_at']}")
        print("-" * 40)

def update_task(task_id,description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task {task_id} not found.")
    
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully.")
            return
    print(f"Task {task_id} not found.")
    
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")

def list_done():
    tasks = load_tasks()
    done_tasks = [task for task in tasks if task["status"] == "done"]
    if not done_tasks:
        print("No done tasks found.")
        return
    for task in done_tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created At: {task['created_at']}")
        print(f"Updated At: {task['updated_at']}")
        print("-" * 40)

def list_todo():
    tasks = load_tasks()
    todo_tasks = [task for task in tasks if task["status"] == "todo"]
    if not todo_tasks:
        print("No todo tasks found.")
        return
    for task in todo_tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created At: {task['created_at']}")
        print(f"Updated At: {task['updated_at']}")
        print("-" * 40)

def list_in_progress():
    tasks = load_tasks()
    in_progress_tasks = [task for task in tasks if task["status"] == "in progress"]
    if not in_progress_tasks:
        print("No in progress tasks found.")
        return
    for task in in_progress_tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created At: {task['created_at']}")
        print(f"Updated At: {task['updated_at']}")
        print("-" * 40)

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in progress"
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} marked as in progress.")
            return
    print(f"Task {task_id} not found.")

if __name__ == "__main__":
    initialize_file()
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <task_description>")
    else:
        command = sys.argv[1]
        if command == "add":
            if len(sys.argv) < 3:
                print("Please provide a task description.")
            else:
                description = " ".join(sys.argv[2:])
                add_task(description)
        elif command == "list":
            list_tasks()
        elif command == "update":
            if len(sys.argv) < 4:
                print("Please provide a task ID and a new description.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    description = sys.argv[3]
                    update_task(task_id, description)
                except ValueError:
                    print("Task ID must be an integer.")
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Please provide a task ID.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    delete_task(task_id)
                except ValueError:
                    print("Task ID must be an integer.")
        elif command == "done":
            if len(sys.argv) < 3:
                print("Please provide a task ID.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    mark_done(task_id)
                except ValueError:
                    print("Task ID must be an integer.")
        elif command == "list_done":
            list_done()
        elif command == "list_todo":
            list_todo()
        elif command == "list_in_progress":
            list_in_progress()
        elif command == "in_progress":
            if len(sys.argv) < 3:
                print("Please provide a task ID.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    mark_in_progress(task_id)
                except ValueError:
                    print("Task ID must be an integer.")
        else:
            print("Unknown command. Available commands: add, list, update, delete, done, list_done, list_todo, list_in_progress, in_progress")
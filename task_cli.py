import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

#Checks if json file exists, if it does, loads into f
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

#Opens json in write then writes tasks list into it in json format
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

#
def add_task(description):
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    now = datetime.now().isoformat()
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f'ID: {task["id"]} | {task["description"]} | Status: {task["status"]} | Created: {task["createdAt"]} | Updated: {task["updatedAt"]}')

def update_tasks(id, description):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if str(task["id"]) == str(id):
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Task {id} updated successfully.")
    else:
        print(f"No task found with ID {id}.")

def delete_task(id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if str(task["id"]) != str(id)]
    if len(new_tasks) == len(tasks):
        print(f"No task found with ID {id}.")
    else:
        save_tasks(new_tasks)
        print(f"Task {id} deleted successfully.")

def mark_in_progress(id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if str(task["id"]) == str(id):
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Task {id} marked as in-progress.")
    else:
        print(f"No task found with ID {id}.")

def mark_done(id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if str(task["id"]) == str(id):
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Task {id} marked as done.")
    else:
        print(f"No task found with ID {id}.")




def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task-cli add \"description\"")
            return
        description = sys.argv[2]
        add_task(description)
    elif command == "list":
        if len(sys.argv) == 3:
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> \"new description\"")
            return
        id = sys.argv[2]
        description = sys.argv[3]
        update_tasks(id, description)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
            return
        id = sys.argv[2]
        delete_task(id)
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <id>")
            return
        id = sys.argv[2]
        mark_in_progress(id)
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <id>")
            return
        id = sys.argv[2]
        mark_done(id)

    # More commands will go here

if __name__ == "__main__":
    main()

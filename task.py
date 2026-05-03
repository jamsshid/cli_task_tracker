import json
import os
import sys
from datetime import datetime

DATE_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATE_FILE):
        return []
    try:
        with open(DATE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    with open(DATE_FILE, "w") as f:
        return json.dump(tasks, f, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "created": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "updated": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added succesfully! ID: {new_task['id']}")

def update_task(task_id, desciption):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = desciption
            task['updated'] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task['id']} updated.")
            return
    print(f"Error: {task_id} not found")

def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task['id']} status marked as {task["status"]}.")
            return
    print(f"Error: {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task['id']} deleted.")
            return
    print(f"Error: {task_id} not found")


def list_tasks(filter=None):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task['status'] == filter] if filter else tasks

    if not filtered_tasks:
        print("No tasks found.")
        return

    template_text = f"{'ID':<5} {'Status':<8} {'Created':<25} {'Updated':<25} {'Description'}"
    print(f"{template_text} \n{'-'*len(template_text)}")
    for task in filtered_tasks:
        print(f"{task['id']:<5} {task['status']:<8} {task['created']:<25} {task['updated']:<25} {task['description']}")

def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python task.py [command] [arguments]\n\nThe commands: add, update, status, list, delete\n"
        )
        print("""Examples:
- Add a task: python task.py add "Buy coffee"
- Update a task: python task.py update 1 "Buy capuchino"
- Change status: python task.py status 1 done
- List all tasks: python task.py list
- Filter tasks by status: python task.py list done
- Delete a task: python task.py delete 1""")

        return

    command = sys.argv[1].lower()

    if command == 'add' and len(sys.argv) >2:
        add_task(sys.argv[2])

    elif command == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "status" and len(sys.argv) > 3:
        change_status(int(sys.argv[2]), sys.argv[3])

    elif command == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()

# Task Manager CLI

A simple and lightweight command-line task manager written in Python.

## Features

- Add new tasks with an automatically generated ID.
- Update existing tasks' descriptions.
- Change task statuses (e.g., `todo`, `in-progress`, `done`).
- Delete tasks when you no longer need them.
- List all tasks or filter them by status with a neat, formatted table.
- Persistent storage automatically managed using a local `tasks.json` file.

## Requirements

- Python 3.x (no external libraries or dependencies required).

## Installation & Setup

1. Create a new directory and navigate into it using your terminal.
2. Save the provided Python script as `task.py`.
3. The script will automatically create a `tasks.json` file in the same folder the first time you add a task.

## Usage

### 1. Add a Task

Adds a new task to your list and assigns a unique ID. New tasks default to `todo` status.

```bash
python task.py add "Buy coffee"
```

**Output:**
```
Task added succesfully! ID: 1
```

---

### 2. Update a Task

Updates the description of an existing task by its ID.

```bash
python task.py update 1 "Buy cappuccino"
```

**Output:**
```
Task 1 updated.
```

---

### 3. Change Status

Updates the status of a task by its ID. Accepted values: `todo`, `in-progress`, `done`.

```bash
python task.py status 1 done
```

**Output:**
```
Task 1 status marked as done.
```

---

### 4. List Tasks

Displays all tasks in a tabular view with ID, status, timestamps, and description.

```bash
python task.py list
```

**Output:**
```
ID    Status   Created                   Updated                   Description
---------------------------------------------------------------------------
1     done     01/06/2024, 08:00:00      01/06/2024, 09:15:00      Buy cappuccino
2     in-progress  01/06/2024, 09:00:00  01/06/2024, 10:02:33      Write unit tests
3     todo     01/06/2024, 08:45:00      01/06/2024, 08:45:00      Update README
```

---

### 5. Filter Tasks

Displays only tasks matching a specific status.

```bash
python task.py list todo
```

**Output:**
```
ID    Status   Created                   Updated                   Description
---------------------------------------------------------------------------
3     todo     01/06/2024, 08:45:00      01/06/2024, 08:45:00      Update README
```

---

### 6. Delete a Task

Removes a task from your list by its ID.

```bash
python task.py delete 1
```

**Output:**
```
Task 1 deleted.
```

---

## Help Menu

Run the script without any arguments to see the help menu:

```bash
python task.py
```

**Output:**
```
Usage: python task.py [command] [arguments]

The commands: add, update, status, list, delete

Examples:
- Add a task: python task.py add "Buy coffee"
- Update a task: python task.py update 1 "Buy capuchino"
- Change status: python task.py status 1 done
- List all tasks: python task.py list
- Filter tasks by status: python task.py list done
- Delete a task: python task.py delete 1
```

---

## Error Handling

If a task ID is not found, the script will print an error:

```
Error: 99 not found
```

If an invalid command or missing arguments are provided:

```
Invalid command or missing arguments.
```
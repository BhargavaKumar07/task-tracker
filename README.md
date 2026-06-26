# Task Tracker CLI

A simple Command Line Interface (CLI) application built with Python to manage tasks. This application allows users to add, update, delete, and track the status of tasks while storing data in a local JSON file.

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as **In Progress**
- Mark a task as **Done**
- List all tasks
- List tasks by status:
  - Todo
  - In Progress
  - Done
- Automatically creates `tasks.json` if it does not exist

## Technologies Used

- Python 3
- JSON
- File Handling
- Command Line Interface (CLI)

## Project Structure

```
task-tracker/
│── task_cli.py
│── README.md
│── .gitignore
└── tasks.json (created automatically)
```

## How to Run

Clone the repository

```bash
git clone https://github.com/BhargavaKumar07/task-tracker
```

Go to the project directory

```bash
cd task-tracker
```

Run commands

### Add a task

```bash
python task_cli.py add "Buy groceries"
```

### Update a task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as In Progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as Done

```bash
python task_cli.py mark-done 1
```

### List all tasks

```bash
python task_cli.py list
```

### List completed tasks

```bash
python task_cli.py list done
```

### List todo tasks

```bash
python task_cli.py list todo
```

### List in-progress tasks

```bash
python task_cli.py list in-progress
```

## Task Properties

Each task contains:

- ID
- Description
- Status
- Created At
- Updated At

## Future Improvements

- Search tasks
- Due dates
- Task priorities
- Categories
- Colored terminal output

## Author
https://github.com/BhargavaKumar07/task-tracker
https://roadmap.sh/projects/task-tracker?fl=1

Bhargava Kumar

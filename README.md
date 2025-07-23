# TaskTracker CLI

A simple command-line tool for managing your personal tasks. Tasks are stored locally in a JSON file (`tasks.json`).

## Features
- Add new tasks with a description
- List all tasks, or filter by status (`todo`, `in-progress`, `done`)
- Update the description of existing tasks
- Delete tasks by their ID
- Mark tasks as "in-progress" or "done"
- Tracks creation and update timestamps for each task

## Usage

Run the script using Python:

```sh
python task_cli.py <command> [arguments]
```

### Commands

- `add "description"` — Add a new task
- `list` — List all tasks
- `list <status>` — List tasks filtered by status (`todo`, `in-progress`, `done`)
- `update <id> "new description"` — Update the description of a task
- `delete <id>` — Delete a task by its ID
- `mark-in-progress <id>` — Mark a task as in-progress
- `mark-done <id>` — Mark a task as done

### Examples

```sh
python task_cli.py add "Buy groceries"
python task_cli.py list
python task_cli.py list done
python task_cli.py update 1 "Buy groceries and cook dinner"
python task_cli.py delete 2
python task_cli.py mark-in-progress 3
python task_cli.py mark-done 3
```

## Notes
- All tasks are stored in `tasks.json` in the same directory as the script.
- Make sure you have Python 3 installed.

## License
MIT License

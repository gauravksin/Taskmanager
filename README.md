# Task Manager

A simple Task Management application built with Python that supports both a Command-Line Interface (CLI) and a REST API using FastAPI.

Tasks are stored persistently in a JSON file, allowing users to create, view, complete, and delete tasks.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Persistent storage using JSON
* Command-line interface
* REST API with FastAPI

## Installation

### Clone the repository

```bash
git clone https://github.com/gauravksin/Taskmanager.git
cd Taskmanager
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the CLI Application

Start the command-line task manager:

```bash
python main.py
```

Example menu:

```text
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
```

## Running the FastAPI Server

Start the API server:

```bash
uvicorn api:app --reload
```

Server will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Add Task

```http
POST /tasks/add
```

Query Parameter:

```text
task=Learn FastAPI
```

Example:

```http
POST /tasks/add?task=Learn FastAPI
```

### Get All Tasks

```http
GET /tasks
```

### Complete Task

```http
POST /tasks/complete
```

Query Parameter:

```text
index=1
```

Example:

```http
POST /tasks/complete?index=1
```

### Delete Task

```http
DELETE /tasks/delete
```

Query Parameter:

```text
index=1
```

Example:

```http
DELETE /tasks/delete?index=1
```

## Example Task Format

Tasks are stored in JSON format:

```json
[
  {
    "name": "Learn FastAPI",
    "done": false
  },
  {
    "name": "Build a Task Manager",
    "done": true
  }
]
```

## Technologies Used

* Python
* FastAPI
* JSON File Storage
* Uvicorn

## Future Improvements

* Task priorities
* Due dates
* Task categories
* SQLite database support
* User authentication
* Docker support
* Unit tests

## License

This project is open source and available under the MIT License.


# TodoFastAPI

A FastAPI-based task management API where users can register, log in, create task groups, and manage their personal to-do tasks.

## Overview

This backend project allows users to:

- Register and log in with secure JWT-based authentication
- Create custom task groups
- Create, update, delete tasks associated with groups
- Mark tasks as complete or incomplete
- Filter tasks by group or completion status

Built using FastAPI and PostgreSQL with SQLAlchemy as the ORM.

---

## Features

### ✅ Authentication
- `POST /register`: Create a new user account
- `POST /login`: Authenticate user and return JWT token

### ✅ Task Groups
- `POST /groups`: Create a new group
- `GET /groups`: Retrieve all groups for the logged-in user
- `GET /groups/{id}`: Retrieve a single group
- `PUT /groups/{id}`: Update group name
- `DELETE /groups/{id}`: Delete a group

### ✅ Tasks
- `POST /tasks`: Create a new task (linked to a group)
- `GET /tasks`: Retrieve tasks (filterable by `?group=<id>` or `?completed=true`)
- `GET /tasks/{id}`: Retrieve a single task
- `PUT /tasks/{id}`: Update title, description, completion status, group
- `DELETE /tasks/{id}`: Delete a task

---

## Data Models

### User
- `id`: Primary Key
- `username`: Unique, required
- `email`: Unique, required
- `password_hash`: Hashed password

### Group
- `id`: Primary Key
- `name`: Required
- `user_id`: FK → User
- `created_at`, `updated_at`: Timestamps

### Task
- `id`: Primary Key
- `title`: Required
- `description`: Optional
- `is_completed`: Boolean, default False
- `user_id`: FK → User
- `group_id`: FK → Group
- `created_at`, `updated_at`: Timestamps

---

## Tech Stack

- Python 3.9+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (PyJWT)
- Passlib (bcrypt)
- Uvicorn

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/M-Adeel-aslam/todo-fastapi.git
cd todo-fastapi
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up `.env` File
Create a `.env` file with the following:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
EXPIRE_TOKEN_TIME=100
KEY=your_secret_key
ALGORITHM=HS256
```

### 5. Run the App
```bash
uvicorn app.main:app --reload
```

---

## Notes

- Ensure PostgreSQL is running and the database mentioned in `.env` exists.
- Only authenticated users can manage their own tasks and groups.
- Passwords are hashed using bcrypt.
- Uses relationships:
  - User → Tasks: one-to-many
  - User → Groups: one-to-many
  - Group → Tasks: one-to-many

---

## Documentation

Once the app is running, access the automatic documentation at:
```
http://localhost:8000/docs
```

---

## License

This project is for academic and learning purposes only.

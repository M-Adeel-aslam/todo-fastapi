# TodoFastAPI

A FastAPI-based backend project where users can register, log in, and manage their own tasks. Each task belongs to a user-defined group.

## Features

- User registration and login using JWT authentication
- Each user can create multiple groups
- Each group can have multiple tasks
- Users can:
  - Create, retrieve, update, delete tasks
  - Mark tasks as complete/incomplete
  - Filter tasks by group or completion status
- Secure password hashing using Passlib
- PostgreSQL database with SQLAlchemy ORM

## Technologies Used

- **Python 3.9+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **JWT (PyJWT)**
- **Passlib (bcrypt)**
- **Uvicorn**

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/M-Adeel-aslam/todo-fastapi.git
   cd todo-fastapi

2. **Create and activate a virtual environment (or use Anaconda)
```bash
conda create -n todoenv python=3.9
conda activate todoenv
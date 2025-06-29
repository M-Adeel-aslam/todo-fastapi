from fastapi import APIRouter, HTTPException, Depends
import models, schema
from datetime import datetime
from auth import verify_current_user
from database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Query

route = APIRouter(
    prefix="/tasks",
    tags=['Task']
)

@route.post("/", response_model=schema.TaskCreateOut)
async def create_tasks(task: schema.TaskCreate, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    new_task = models.Task(
        user_id=current_user["id"],
        title=task.title,
        description=task.description,
        group_id=task.group_id,
        is_completed=task.is_completed,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@route.get("/", response_model=List[schema.TaskCreateOut])
async def list_all_tasks(group: Optional[int] = Query(None),completed: Optional[bool] = Query(None),db: Session = Depends(get_db),current_user: dict = Depends(verify_current_user)):
    query = db.query(models.Task).filter(models.Task.user_id == current_user["id"])
    if group is not None:
        query = query.filter(models.Task.group_id == group)
    if completed is not None:
        query = query.filter(models.Task.is_completed == completed)
    return query.all()


@route.get("/{id}", response_model=schema.TaskCreateOut)
async def get_task_by_id(id: int, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id, models.Task.user_id == current_user["id"]).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@route.put("/{id}", response_model=schema.TaskCreateOut)
async def update_task(id: int, updated_task: schema.TaskCreate, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id, models.Task.user_id == current_user["id"]).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")

    task.title = updated_task.title
    task.description = updated_task.description
    task.is_completed = updated_task.is_completed
    task.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(task)
    return task

@route.delete("/{id}")
async def delete_task(id: int, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id, models.Task.user_id == current_user["id"]).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")

    db.delete(task)
    db.commit()
    return {"message": f"Task with ID {id} has been deleted"}
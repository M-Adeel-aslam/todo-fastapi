from fastapi import APIRouter, HTTPException, Depends
import models, schema
from datetime import datetime
from auth import verify_current_user
from database import get_db
from sqlalchemy.orm import Session
from typing import List

route = APIRouter(
    prefix="/groups",
    tags=['Group']
)

@route.post("/", response_model=schema.GroupCreateOut)
async def create_group(group: schema.GroupCreate, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    existing_group = db.query(models.Group).filter(models.Group.name == group.name).first()
    if existing_group:
        raise HTTPException(status_code=400, detail="Group already exists.")
    
    new_group = models.Group(
        name=group.name,
        user_id=current_user["id"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group


@route.get("/", response_model=List[schema.GroupCreateOut])
async def list_all_groups(db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    groups = db.query(models.Group).filter(models.Group.user_id == current_user["id"]).all()
    return groups

@route.get("/{id}", response_model=schema.GroupCreateOut)
async def get_group_by_id(id: int, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    group = db.query(models.Group).filter(models.Group.id == id, models.Group.user_id == current_user["id"]).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found or unauthorized")
    return group


@route.put("/{id}", response_model=schema.GroupCreateOut)
async def update_group(id: int, updated_group: schema.GroupCreate, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    group = db.query(models.Group).filter(models.Group.id == id, models.Group.user_id == current_user["id"]).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found or unauthorized")
    
    group.name = updated_group.name
    group.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(group)
    return group


@route.delete("/{id}")
async def delete_group(id: int, db: Session = Depends(get_db), current_user: dict = Depends(verify_current_user)):
    group = db.query(models.Group).filter(models.Group.id == id, models.Group.user_id == current_user["id"]).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found.")

    db.delete(group)
    db.commit()
    return {"message": f"Group with ID {id} has been deleted"}
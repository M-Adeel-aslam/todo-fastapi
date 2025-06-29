from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class Usercreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr

    class Config():
        orm_mode=True

# groups
class GroupCreate(BaseModel):
    name:str

class GroupCreateOut(GroupCreate):
    id:int
    user_id:int
    created_at:datetime
    updated_at:datetime
    class Config():
        orm_mode=True

# tasks
class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    is_completed:bool=False
    group_id:int

class TaskCreateOut(TaskCreate):
    id:int
    user_id:int
    created_at:datetime
    updated_at:datetime
    class Config():
        orm_mode=True


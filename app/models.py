from sqlalchemy import Column, String, Integer,Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, nullable=False, unique=True)
    email=Column(String, nullable=False, unique=True)
    password=Column(String, nullable=False)

    groups = relationship("Group", back_populates="user")
    tasks = relationship("Task", back_populates="user")


class Group(Base):
    __tablename__="groups"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    user_id=Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    
    user = relationship("User", back_populates="groups")
    tasks = relationship("Task", back_populates="group")


class Task(Base):
    __tablename__="tasks"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String, nullable=False)
    description=Column(String, nullable=True)
    is_completed =Column(Boolean, default=False)
    user_id=Column(Integer, ForeignKey("users.id"))
    group_id=Column(Integer, ForeignKey("groups.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    
    user = relationship("User", back_populates="tasks")
    group = relationship("Group", back_populates="tasks")

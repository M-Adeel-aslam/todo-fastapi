from fastapi import APIRouter, HTTPException, Depends
from .. import models, schema, database
from fastapi.security import OAuth2PasswordRequestForm
from app.database import create_all_tables, get_db
from sqlalchemy.orm import Session
from app.utils import verify_password, hassed_password
from app.auth import create_access_token

create_all_tables()


route = APIRouter(
    prefix="/auth",
    tags=['Auth']
)

@route.post("/register", response_model=schema.UserOut)
async def register(user:schema.Usercreate, db:Session=Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email== user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="user email already exists!")
    encrpyted_password = hassed_password(user.password)
    newUser = models.User(
        username = user.username,
        email = user.email,
        password = encrpyted_password
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


@route.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Username does not exist")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Password is incorrect")
    
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}


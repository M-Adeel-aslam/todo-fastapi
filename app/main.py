from app.routes import authentication, groups, tasks
from fastapi import FastAPI
from app.database import create_all_tables
create_all_tables()
app = FastAPI()

app.include_router(authentication.route)
app.include_router(groups.route)
app.include_router(tasks.route)


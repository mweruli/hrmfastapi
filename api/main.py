from fastapi import FastAPI
from api.routers import users,companys
from api.db.database import engine
from api.models import data_models


data_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(companys.router)
app.include_router(users.router)
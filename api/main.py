from fastapi import FastAPI
from api.routers import company


app = FastAPI()


app.include_router(company.router)
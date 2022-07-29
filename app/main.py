# app/main.py

from fastapi import FastAPI

from app.db import database, User
from app.models import UserIn, UserOut, UserInDB
from app.endpoints import user_input, user_register

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.post("/user/")
async def read_root(user: UserIn):
    if user.choice:
        user_input(user.hashed_password, user.email,
                   user.price)  # return await User.objects.all()
    else:
        user_register(user.email, user.hashed_password, user.price)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    # await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
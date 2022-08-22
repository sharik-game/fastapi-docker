from fastapi import FastAPI, Query

from fastapi.responses import Response

from app.db import database, User
from app.models import UserIn, UserOut, UserInDB
from app.endpoints import user_input, user_register

# import json
app = FastAPI(title="FastAPI, Docker")

@app.get("/")
def begining(q: bool = Query(default=True)):
    if q:
        with open("app/frontend/login.html", "r") as file_html:
            login_page = file_html.read()
    else:
        with open("app/frontend/register.html", "r") as file_html2:
            login_page = file_html2.read()
    return Response(login_page, media_type='text/html')
@app.post("/user/")
async def read_root(user_in: UserIn):
    if user_in.dict()["choice"]:
        try:
            return await user_input(user_in)  # return await User.objects.all()
        except Exception as ex:
            print("..mistake :(")
            print(str(ex))
            return {"input": False}
    else:
        await user_register(user_in)
        return await User.objects.all()


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
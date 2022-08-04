from app.db import database, User
from app.models import UserInDB, UserIn, UserOut


async def user_input(user_in: UserIn):
    user_in2 = user_in.dict()
    # answer = False
    
    check = await User.objects.get(User.hashed_password == user_in2["hashed_password"])
    # email_in_out = await User.objects.get(User.email == user_in2["email"])
    # price_in_out = await User.objects.get(User.price == user_in2["price"])
    print(check)
    user_output = UserOut(**check.dict())
    return user_output
    # answer = user_output
    # return user_output
    # answer = user_output
    
    # return {"input": False}
    # return answer
        


async def user_register(user_in: UserIn):
    user_in_db = UserInDB(email = user_in.dict()["email"], hashed_password = user_in.dict()["hashed_password"], price = user_in.dict()["price"])
    # await User.objects.create(email = user_in_db.dict()["email"], hashed_password = user_in_db.dict()["hashed_password"], price = user_in_db.dict()["price"])
    await User.objects.create(**user_in_db.dict())
    # return {"register": True}

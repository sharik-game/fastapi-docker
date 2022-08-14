from app.db import database, User
from app.models import UserInDB, UserIn, UserOut
from app.hashing import Hasher

async def user_input(user_in: UserIn):
    user_in2 = user_in.dict()
    email_in_out = await User.objects.get(User.email == user_in2["email"])
    check_password = Hasher.verify_password(user_in2["hashed_password"], email_in_out.dict()["hashed_password"])
    if check_password:
        user_output = UserOut(**email_in_out.dict())
        return user_output
    else:
        raise KeyError
    
        


async def user_register(user_in: UserIn):
    user_in_db = UserInDB(email = user_in.dict()["email"], hashed_password = Hasher.get_password_hash(user_in.dict()["hashed_password"]), price = user_in.dict()["price"])
    await User.objects.create(**user_in_db.dict())
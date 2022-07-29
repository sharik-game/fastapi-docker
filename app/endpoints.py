from app.db import database, User
from app.models import UserOut


async def user_input(password_check: str, email_in: str, price_in: int):
    try:
        check = await User.object.get(User.hashed_password == password_check)
        email_in_out = await User.object.get(User.email == email_in)
        price_in_out = await User.object.get(User.price == price_in)
        print(check)
        user_output = UserOut(email=email_in_out, price=price_in_out)
        return user_output
    except Exception as ex:
        print("mistake :(")
        print(str(ex))
        return False


async def user_register(email_r: str, hashed_password_r: str, price_r: int):
    await User.object.get_or_create(email=email_r,
                                    hashed_password=hashed_password_r,
                                    price=price_r)
    return {"register": True}

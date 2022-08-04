from pydantic import BaseModel, Field


class UserIn(BaseModel):
    email: str
    hashed_password: str
    choice: bool | None # 1 - input, 0 - register
    price: int | None


class UserOut(BaseModel):
    email: str
    price: int


class UserInDB(BaseModel):
    email: str
    hashed_password: str
    price: int = Field(default=0)

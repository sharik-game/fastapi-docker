from pydantic import BaseModel, Field


class UserIn(BaseModel):
    email: str
    hashed_password: str
    choice: bool = Field(description="0 - register, 1 - input")
    price: int


class UserOut(BaseModel):
    email: str
    price: int


class UserInDB(BaseModel):
    email: str
    hashed_password: str
    price: int = Field(default=0)

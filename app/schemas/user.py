from typing import Optional

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str


class UserCreateSchema(UserBaseSchema):
    salary : Optional[float]


class UserResponseSchema(UserBaseSchema):
    user_id: int
    salary : float

    class Config:
        orm_mode = True   
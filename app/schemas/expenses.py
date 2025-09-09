from datetime import datetime

from pydantic import BaseModel, Field

from app.models import CategoryEnum

class ExpensesBaseSchema(BaseModel):
    user_id: int
    name: str
    amount: float = Field(gt=0)
    category: CategoryEnum

    class Config:
        orm_mode = True 


class ExpeneCreateSchema(ExpensesBaseSchema):
    pass


class ExpenseResponseSchema(ExpensesBaseSchema):
    created_at : datetime


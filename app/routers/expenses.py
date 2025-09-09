from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import Expense
from app.dependencies import get_db
from app.schemas.expenses import ExpeneCreateSchema, ExpenseResponseSchema

router = APIRouter(prefix="/expenses")


@router.post("/create-expense", response_model=ExpenseResponseSchema)
async def create_expense(expense: ExpeneCreateSchema, db: Session = Depends(get_db)):
    expense_model = Expense(**expense.model_dump())
    db.add(expense_model)
    db.commit()
    db.refresh(expense_model)
    return expense_model
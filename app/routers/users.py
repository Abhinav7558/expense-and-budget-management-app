from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import User, Expense
from app.dependencies import get_db
from app.schemas.user import UserBaseSchema, UserCreateSchema, UserResponseSchema

router = APIRouter(prefix="/users")

@router.post("/create-user", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user_model = User(**user.model_dump())
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model

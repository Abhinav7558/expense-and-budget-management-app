import enum  

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime, func
from app.database import Base


class CategoryEnum(enum.Enum):
   FOOD = "food"
   TRANSPORT = "transport"
   ENTERTAINMENT = "entertainment"
   UTILITIES = "utilities"
   OTHER = "other"


class User(Base):
   __tablename__ = "user"
   user_id = Column(Integer, primary_key=True, autoincrement=True)
   username = Column(String, unique=True, nullable=False)
   salary = Column(Float, default=0.0)


class Expense(Base):
   __tablename__ = "expenses"
   expense_id = Column(Integer, primary_key=True, autoincrement=True)
   user_id = Column(Integer, ForeignKey("user.user_id"))
   name = Column(String, nullable=False)
   amount = Column(Float)
   category = Column(
      Enum(CategoryEnum, name="category_enum")
   )
   created_at = Column(DateTime(timezone=True), server_default=func.now())
   

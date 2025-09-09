from fastapi import FastAPI
from app.routers.expenses import router as expense_router
from app.routers.totals import router as totals_router
from app.routers.users import router as users_router

app = FastAPI()

app.include_router(expense_router)
app.include_router(totals_router)
app.include_router(users_router)

@app.get("/health")
def health_check():
    """End point for health check"""
    return {"status": "ready"}
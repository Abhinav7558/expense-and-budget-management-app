from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    """End point for health check"""
    return {"status": "ready"}
import uvicorn
from fastapi import FastAPI
from app.database.database import db
from app.adapters.api import task_routes

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await db.connect()


@app.on_event("shutdown")
async def shutdown_event():
    await db.close()


app.include_router(task_routes.router, tags=["Tasks"], prefix="/api/v1/task")


@app.get("/", include_in_schema=False)
async def get_root():
    return {"message": "Welcome to FastAPI Clean Architecture"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

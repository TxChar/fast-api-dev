from fastapi import APIRouter, Depends, HTTPException
from app.core.models import TaskCreate, TaskUpdate
from app.core.use_cases import TaskService
from app.adapters.repositories.task_repo import TaskRepository

router = APIRouter()
task_service = TaskService(TaskRepository())


@router.get("/", response_description="List all Tasks")
async def list_tasks():
    return await task_service.list_tasks()


@router.post("/", response_description="Create a Task")
async def create_task(task: TaskCreate):
    task_id = await task_service.create_task(task)
    return {"id": task_id}


@router.patch("/{id}", response_description="Update a Task")
async def update_task(id: str, task: TaskUpdate):
    success = await task_service.update_task(id, task)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to update task.")
    return {"message": "Task updated"}


@router.delete("/{id}", response_description="Delete task")
async def delete_task(id: str):
    success = await task_service.delete_task(id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}

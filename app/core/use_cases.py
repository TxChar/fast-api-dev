from app.core.models import TaskBase, TaskCreate, TaskUpdate
from app.adapters.repositories.task_repo import TaskRepository


class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def list_tasks(self):
        return await self.task_repo.get_all()

    async def create_task(self, task: TaskCreate):
        return await self.task_repo.create(task)

    async def update_task(self, task_id: str, task: TaskUpdate):
        return await self.task_repo.update(task_id, task)

    async def delete_task(self, task_id: str):
        return await self.task_repo.delete(task_id)

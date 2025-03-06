from app.core.models import TaskBase, TaskCreate, TaskUpdate
from app.database.database import db
from bson import ObjectId


class TaskRepository:
    async def get_all(self):
        tasks = []
        async for task in db.db["tasks"].find():
            tasks.append(TaskBase(**task))
        return tasks

    async def create(self, task: TaskCreate):
        task_dict = task.dict(by_alias=True)
        new_task = await db.db["tasks"].insert_one(task_dict)
        return str(new_task.inserted_id)

    async def update(self, task_id: str, task: TaskUpdate):
        updated_result = await db.db["tasks"].update_one(
            {"_id": ObjectId(task_id)},
            {"$set": task.dict(exclude_unset=True, by_alias=True)},
        )
        return updated_result.modified_count > 0

    async def delete(self, task_id: str):
        delete_result = await db.db["tasks"].delete_one({"_id": ObjectId(task_id)})
        return delete_result.deleted_count > 0

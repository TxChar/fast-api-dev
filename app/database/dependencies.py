# from fastapi import Depends
# from app.adapters.repositories.task_repo import TaskRepository
# from app.core.use_cases import TaskService
# from app.database.database import db


# # ✅ Dependency Injection ให้ FastAPI ใช้ TaskRepository
# def get_task_repository():
#     return TaskRepository()


# # ✅ Inject TaskService โดยใช้ TaskRepository
# def get_task_service(task_repo: TaskRepository = Depends(get_task_repository)):
#     return TaskService(task_repo)


# async def get_database():
#     if db.client is None:
#         await db.connect()
#     return db.db

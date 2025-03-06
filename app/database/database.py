from motor.motor_asyncio import AsyncIOMotorClient
from app.database.config import settings


class Database:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_NAME]

    async def close(self):
        if self.client:
            self.client.close()


db = Database()

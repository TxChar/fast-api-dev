from typing import Union
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import Optional

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")

db = client["votes"]
collection = db["votes"]


class Vote(BaseModel):
    name: str
    count: int = Field(default=0)
    is_deleted: Optional[bool] = Field(default=False, exclude=True)

    class Config:
        schema_extra = {"example": {"name": "string", "count": 0}}


@app.get("/")
def read_root():
    return {"Message": "Hello World"}


# Create
@app.post("/votes/")
async def create_vote(vote: Vote):
    result = collection.insert_one(vote.dict())
    return {
        "id": str(result.inserted_id),
        "name": vote.name,
        "count": vote.count,
    }


@app.get("/votes/{vote_id}")
async def get_vote(vote_id: str):
    vote = collection.find_one(
        {"_id": ObjectId(vote_id), "is_deleted": False}
    )  # ดึงเฉพาะที่ยังไม่ถูกลบ
    if vote:
        return {
            "id": str(vote["_id"]),
            "name": vote["name"],
            "count": vote["count"],
        }
    else:
        raise HTTPException(status_code=404, detail="Vote not found")


@app.put("/votes/{vote_id}")
async def update_vote(vote_id: str, vote: Vote):
    result = collection.update_one(
        {"_id": ObjectId(vote_id)},
        {"$set": vote.dict(exclude_unset=True)},
    )

    if result.modified_count == 1:
        return {
            "id": vote_id,
            "name": vote.name,
            "count": vote.count,
        }
    else:
        raise HTTPException(status_code=404, detail="Vote not found")


@app.delete("/votes/{vote_id}")
async def delete_vote(vote_id: str):
    result = collection.update_one(
        {"_id": ObjectId(vote_id)}, {"$set": {"is_deleted": True}}
    )

    if result.modified_count == 1:
        return {"message": "Vote deleted", "id": vote_id}
    else:
        raise HTTPException(status_code=404, detail="Vote not found or already deleted")

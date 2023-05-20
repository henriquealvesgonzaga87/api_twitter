from fastapi import FastAPI
from src.services import get_trends
import uvicorn
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.dio_live

trends_collection = db.trends


class TrendItem(BaseModel):
    name: str
    url: str


BRAZIL_WOE_ID = 23424768

app = FastAPI()


@app.get("/trends", response_model=list[TrendItem])
def get_trends_route():

    trends = trends_collection.find({})

    return list(trends)


if __name__ == "__main__":
    trends = trends_collection.find({})

    if not list(trends):
        trend = get_trends(woe_id=BRAZIL_WOE_ID)
        trends_collection.insert_many(trend)

    uvicorn.run(app, host="0.0.0.0", port=8000)

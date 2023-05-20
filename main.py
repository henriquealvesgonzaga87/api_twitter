from fastapi import FastAPI
from src.services import get_trends
import uvicorn
from pydantic import BaseModel

#client = MongoClient("")

#db = client.my_test

#tweets_collection = db.tweets

#tweets_collection.insert_one({"author": "test", "text": "text"})

#tweets = tweets_collection.find({})

#print(list(tweets))


class TrendItem(BaseModel):
    name: str
    url: str


BRAZIL_WOE_ID = 23424768

app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    trend = get_trends(woe_id=BRAZIL_WOE_ID)

    return trend


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

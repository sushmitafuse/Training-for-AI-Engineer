import uvicorn
from fastapi import FastAPI, Request
import motor.motor_asyncio


app = FastAPI()

MONGO_DETAILS =  "mongodb://localhost:27017/emotion_data"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.emotion_data

emotion_collection = database.get_collection("users")
print(emotion_collection)


#helper
def emotion_helper(emotion) -> dict:
    return {
        "id": str(emotion["_id"]),
        "text": emotion["text"],
        "model": emotion["model"],
        "emotion": emotion["emotion"],
        "confidence": emotion["confidence"],
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/emotions")
async def retrieve_emotions():
    emotions = []
    async for emotion in emotion_collection.find():
        emotions.append(emotion_helper(emotion))
    return emotions


if __name__ == "__main__":
    app.run(debug=True)

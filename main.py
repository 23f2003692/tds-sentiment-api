from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CommentRequest(BaseModel):
    comment: str

@app.post("/comment")
async def analyze_comment(data: CommentRequest):
    if not data.comment.strip():
        raise HTTPException(status_code=400, detail="Comment cannot be empty")

    text = data.comment.lower()

    positive_words = ["good", "great", "amazing", "excellent", "love", "awesome", "fantastic"]
    negative_words = ["bad", "worst", "terrible", "hate", "awful", "poor"]

    sentiment = "neutral"
    rating = 3

    if any(word in text for word in positive_words):
        sentiment = "positive"
        rating = 5
    elif any(word in text for word in negative_words):
        sentiment = "negative"
        rating = 1

    return {
        "sentiment": sentiment,
        "rating": rating
    }
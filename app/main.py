from fastapi import FastAPI
from utils.qna import qna_bot
from pydantic import BaseModel
app = FastAPI()

class QuestionPayload(BaseModel):
    question: str

@app.post("/qna")
async def qna(payload: QuestionPayload):
    response = qna_bot(payload.question)
    return response
from fastapi import FastAPI
from utils.qna import qna_bot

app = FastAPI()

@app.post("/qna")
async def qna(question: str):
    response = qna_bot(question)
    return response
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.rag import get_answer_and_docs
from src.qdrant import upload_website_to_collection

app = FastAPI(
    title="RAG API",
    description="A simple RAG API",
    version="0.1",
)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

class IndexingRequest(BaseModel):
    url: str

@app.post('/chat', description="Chat with your RAG API")
def chat(message: Message):
    response = get_answer_and_docs(message.message)
    response_content = {
        "question": message.message,
        "answer": response["answer"],
        "documents": [doc.dict() for doc in response["context"]]
    }
    return JSONResponse(content=response_content, status_code=200)

@app.post('/indexing', description="Index a website through endpoint")
def indexing(request: IndexingRequest):
    try:
        upload_website_to_collection(request.url)
        return JSONResponse(content={"response": "Indexing successful"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

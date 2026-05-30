# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import base64
from io import BytesIO
from PIL import Image

from image_retrieval import ImageRetrieval
from config import CHROMA_DB_PATH, MODEL_NAME, COLLECTION_NAME

# Request model
class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

# Initialize FastAPI
app = FastAPI(title="Text-to-Image Retrieval API")

# Initialize the retrieval engine
retriever = ImageRetrieval(
    model_name=MODEL_NAME,
    db_path=CHROMA_DB_PATH,
    collection_name=COLLECTION_NAME
)

@app.post("/search")
def search_images(request: SearchRequest):
    images, scores = retriever.retrieve(request.query, top_k=request.top_k, return_scores=True)
    results = []
    for img, score in zip(images, scores):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        results.append({"image": img_str, "score": score})
    return {"results": results}

@app.get("/stats")
def stats():
    db_stats = retriever.get_stats()
    return {"total_images": db_stats["total_images"], "status": "ready"}
import os
import random
from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CatMemesAPI",
    version="1.2.0",
    description="API with memes about cats"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MEMES_DIR = "memes"


def load_memes():
    """Загружает все мемы из папки и парсит ID из имени файла."""
    memes = []
    if not os.path.exists(MEMES_DIR):
        return memes

    for f in os.listdir(MEMES_DIR):
        if f.lower().endswith(('.jpg')):
            try:
                name_parts = f.replace('.jpg', '')
                meme_id = int(name_parts.replace('meme_cat_', ''))
            except (ValueError, IndexError):
                meme_id = len(memes)

            memes.append({"id": meme_id, "filename": f})

    memes.sort(key=lambda x: x['id'])
    return memes


memes = load_memes()


@app.get("/")
def info():
    """Информация об API."""
    return {
        "title": "CatMemesAPI",
        "version": "1.2.0",
        "total_memes": len(memes),
        "formats": ["jpg"],
        "endpoints": {
            "/": "API info",
            "/meme/search?limit=5": "Get 5 random memes",
            "/meme/{meme_id}": "Get meme by ID"
        }
    }


@app.head("/")
def info_head():
    return Response()


@app.get("/meme/search")
def search_memes(request: Request, limit: int = 1):
    """Возвращает случайные мемы."""
    if not memes:
        return JSONResponse(status_code=404, content={"error": "No memes found"})

    limit = min(limit, len(memes))
    selected = random.sample(memes, limit)

    result = []
    for m in selected:
        filepath = os.path.join(MEMES_DIR, m['filename'])
        try:
            with Image.open(filepath) as img:
                width, height = img.size
        except Exception:
            width, height = 0, 0

        full_url = str(request.url_for("get_meme_by_id", meme_id=m["id"]))

        result.append({
            "id": m["id"],
            "url": full_url,
            "width": width,
            "height": height
        })
    return result


@app.head("/meme/search")
def search_memes_head():
    return Response()


@app.get("/meme/{meme_id}")
def get_meme_by_id(meme_id: int):
    """Возвращает мем по ID."""
    for m in memes:
        if m["id"] == meme_id:
            filepath = os.path.join(MEMES_DIR, m['filename'])
            if os.path.exists(filepath):
                return FileResponse(filepath)
            return JSONResponse(status_code=404, content={"error": "File not found"})

    return JSONResponse(status_code=404, content={"error": "Meme not found"})


@app.head("/meme/{meme_id}")
def get_meme_by_id_head(meme_id: int):
    """HEAD-запрос для проверки существования мема."""
    for m in memes:
        if m["id"] == meme_id:
            filepath = os.path.join(MEMES_DIR, m['filename'])
            if os.path.exists(filepath):
                return Response()
    return Response(status_code=404)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.head("/health")
def health_head():
    return Response()

from typing import Optional

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/upload-file/")
async def create_upload_file(file: UploadFile = File(...)):
    print(file.filename)
    return {"filename": file.filename}


@app.get("/watch/")
async def watch(v: Optional[int] = None):
    if v == 2:
        video_stream_file = "media/video2.mp4"
    else:
        video_stream_file = "media/video1.m4v"
    return FileResponse(video_stream_file)

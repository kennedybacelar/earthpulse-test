import os
from fastapi import FastAPI, UploadFile, File
import uvicorn
from .core import write_file, process_image_attributes

__author__ = "Kennedy Bacelar"

app = FastAPI(title="EarthPulse API test")
PORT = os.environ.get("PORT") or 8020


@app.get("/")
def home_():
    return {"message": "Welcome to EarthPulse API test"}


@app.post("/attributes")
async def get_image_attributes_post(image: UploadFile = File(..., alias="file")):
    await write_file()
    process_image_attributes()


@app.post("/thumbnail")
async def get_RGB_thumbnail_post(image: UploadFile = File(..., alias="file")):
    pass


@app.post("/ndvi")
async def get_colored_PNG(image: UploadFile = File(..., alias="file")):
    pass


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=True)

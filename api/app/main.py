import os
from fastapi import FastAPI, UploadFile, File, Form, status
import uvicorn
from .core import write_file, process_image_attributes, create_image_thumbnail

__author__ = "Kennedy Bacelar"

app = FastAPI(title="EarthPulse API test")
PORT = os.environ.get("PORT") or 8020


@app.get("/")
def home_():
    return {"message": "Welcome to EarthPulse API test"}


@app.post("/attributes", status_code=status.HTTP_200_OK)
async def get_image_attributes_post(image: UploadFile = File(..., alias="file")):
    """Get image attributes route"""
    await write_file(image)
    return process_image_attributes()


@app.post("/thumbnail", status_code=status.HTTP_200_OK)
async def get_RGB_thumbnail_post(
    image: UploadFile = File(..., alias="file"),
    width: int = Form(100),
    height: int = Form(100),
):
    """Get RGB thumbnail route"""
    await write_file(image)
    return create_image_thumbnail(max_size=(width, height))


@app.post("/ndvi")
async def get_colored_PNG(image: UploadFile = File(..., alias="file")):
    pass


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=True)

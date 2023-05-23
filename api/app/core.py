from typing import Tuple
import rasterio
import rasterio.features
import rasterio.warp
from matplotlib import cm
import numpy as np
from PIL import Image


DEFAULT_FILENAME = "uploaded_file.tiff"
THUMBNAIL_FILENAME = "thumbnail.png"


async def write_file(image: bytes, filename: str = DEFAULT_FILENAME) -> bool:
    with open(filename, "wb") as file:
        file.write(await image.read())
    return True


def process_image_attributes(filename: str = DEFAULT_FILENAME):
    with rasterio.open(filename) as dataset:
        response_json = {
            "width": dataset.width,
            "height": dataset.height,
            "number_of_bands": dataset.count,
            "crs": dataset.crs.to_dict(),
            "bounding_box": dataset.bounds,
        }
    return response_json


def create_image_thumbnail(
    filename: str = DEFAULT_FILENAME, max_size: Tuple[int, int] = (100, 100)
):
    with Image.open(DEFAULT_FILENAME) as image:
        image.thumbnail(max_size)
        image.save("pythonthumb.png")
        image.show()
    return image

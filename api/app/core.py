import rasterio
import rasterio.features
import rasterio.warp

DEFAULT_FILENAME = "uploaded_file.tiff"


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

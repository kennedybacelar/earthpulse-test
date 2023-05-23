import os
import rasterio
import rasterio.features
import rasterio.warp

DEFAULT_FILENAME = "uploaded_file.tif"


async def write_file(filename: str = DEFAULT_FILENAME) -> bool:
    try:
        with open(filename, "wb") as file:
            file.write(await filename.read())
        return True
    except Exception as error:
        return False


def processing_image_attributes(filename: str = DEFAULT_FILENAME):
    with rasterio.open("example.tif") as dataset:
        mask = dataset.dataset_mask()
        for geom, val in rasterio.features.shapes(mask, transform=dataset.transform):
            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geom = rasterio.warp.transform_geom(
                dataset.crs, "EPSG:4326", geom, precision=6
            )

            print(geom)

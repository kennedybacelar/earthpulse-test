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
        mask = dataset.dataset_mask()
        for geom, val in rasterio.features.shapes(mask, transform=dataset.transform):
            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geom = rasterio.warp.transform_geom(
                dataset.crs, "EPSG:4326", geom, precision=6
            )

            print(geom)

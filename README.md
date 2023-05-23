## API - Processing Satellite Image


The provided API is a FastAPI-based service for image processing and handling. It offers the following features:

Welcome Route: Accepts a GET request at the root ("/") and returns a welcome message.

Image Attributes Route: Accepts a POST request at "/attributes" with an image file. It saves the file, retrieves the attributes of the image using the core module, and returns the attributes as a JSON response.

RGB Thumbnail Route: Accepts a POST request at "/thumbnail" with an image file and optional width and height parameters. It saves the file, creates an RGB thumbnail image with the specified dimensions using the core module, and returns the thumbnail image as a response.

NDVI Route: Accepts a POST request at "/ndvi" with an image file. Currently, the function body is empty, indicating that the implementation is pending.

The API is designed to run using Uvicorn server on host "0.0.0.0" and port 8020. The script also allows for auto-reloading during development.


## Installation and Running with Docker

1. Clone the repository and navigate to the project directory. To start the API in a Docker container run at the root of the project:
    
    ```
    docker-compose up --build
    ```

2. You can run the tests by executing the following command at the root of the project:

    ```
    docker exec earth-pulse python -m pytest -v tests
    ```

    This will execute the tests inside the running container at `tests/` directory.


## Installation and Running without Docker

The application works over an Ubuntu system and with Python 3.10.

1. Clone the repository locally.
2. Navigate to the api/ folder.
3. Install the requirements by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the server by entering the command from the api/ folder:
    ```
    python -m app.main
    ```
5. This will make the server run locally, and the test message can be checked from the browser by hitting the URL http://localhost:8020.
6. To run the tests, also from the api/ directory, enter the command:
    ```
    python -m pytest -v tests


## Testing

You can test the API using the built-in FastAPI tool called Swagger UI. Access the URL http://localhost:8020/docs from your browser to access the interactive API documentation. The Swagger UI allows you to explore and test all the API endpoints by providing sample requests and viewing the responses.
This tutorial walks you through the process
of creating and running a Flask application in a Docker container.

1. **Image Build**:
Use "docker build -t my-python-app ." command
within dockerfile directory to build the Docker image named my-python-app
The image size will be approximately 1.01GB.

2. **Image Verification**:
Use "docker images" command to to list all available Docker images.
Make sure the newly created image my-python-app 
is displayed alongside other existing images.

3. **Container Run**:
Use "docker run -p 5001:5001 --name my-python-app my-python-app" command
to start a container from the my-python-app image.
The Flask application will be running in development mode,
listening on all addresses (0.0.0.0) and accessible via
http://127.0.0.1:5001 or http://localhost:5001/

4. **Requests**: The server received a GET request for the root URL
(/), responding with a status code of 200,
indicating success. Additionally, there was a request for the favicon,
which resulted in a 404 error, as no favicon was provided.


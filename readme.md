### Make sure to install Flask using the pip command in your virtual environment.
` pip install Flask `
### You can run this application using the following command:
` python app.py `
Open your browser and go to http://localhost:5000 to see the "<h1>Simple To-Do App</h1>" message.
### Step 2:  Building a Docker Image
```
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

```

### We also need to create a requirements.txt file in the same directory as app.py to specify the dependencies for the Flask application. 
Flask==2.3.2

#### Now, we can build the Docker image using the following command: 
` docker build -t my-flask-app .`
#### Step 3: Running the Docker Container
` docker run -p 5000:5000 my-flask-app `
### Step 4: Using Docker Compose
If you want to orchestrate multiple containers, you can use Docker Compose. Create a new file called docker-compose.yml in the same directory as app.py.

```
version: "3.9"
services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      FLASK_APP: app.py
      FLASK_ENV: development 
```
You can start the application using Docker Compose using the following command:

`docker-compose up`

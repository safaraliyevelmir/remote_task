# Use the official Python 3.11 image.
FROM python:3.11

# Set the working directory to /code inside the container
WORKDIR /code

# Copy the requirements.txt file to the container and install Python dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code from your host to your container's working directory.
COPY . .

# Set the default command for the container to run your application using Uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

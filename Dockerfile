# Use official Python image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the AI model script
CMD ["python", "app.py"]

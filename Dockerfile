# Use a base image with Python installed
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the local requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local application code to the container
COPY . /app

## Expose the port that Streamlit runs on
#EXPOSE 8501

# Command to run the Streamlit app
#CMD ["python", "./src/app.py"]

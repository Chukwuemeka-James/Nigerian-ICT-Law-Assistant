# lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Install dependencies using Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the entire project into the container
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Define the environment variable for Streamlit to work in a container
ENV STREAMLIT_SERVER_HEADLESS=true

# Run the Streamlit application
CMD ["pipenv", "run", "streamlit", "run", "ICT_Law_Assistant.py"]

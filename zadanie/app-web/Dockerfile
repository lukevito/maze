FROM python:3.9


RUN ls

# Print the current directory to verify activation
RUN pwd

# Echo a message for clarity
RUN echo "Aktualny katalog:" pwd

# Create the virtual environment
RUN python -m venv venv

# Upgrade pip within the virtual environment
RUN venv/bin/pip install --upgrade pip

# Activate the virtual environment using bash shell 
RUN ["bash", "-c", "source venv/bin/activate"]

# Print the current directory to verify activation
RUN pwd

# Echo a message for clarity
RUN echo "Aktualny katalog:"

WORKDIR /app-web

COPY requirements.txt .

# Install dependencies from requirements.txt
RUN ["bash", "-c", "pip install -r requirements.txt"]

COPY . .

# Start the application
CMD ["python", "app.py"]

# Add label for easy identification
LABEL image="maze-app-web"
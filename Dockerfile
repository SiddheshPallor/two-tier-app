# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirement file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# ---------- Env vars for Flask & DB ----------
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# DB settings – container will use these to reach MySQL on your Windows host
ENV DB_HOST=host.docker.internal
ENV DB_PORT=3307
ENV DB_USER=root
ENV DB_PASSWORD=root      
ENV DB_NAME=two_tier_db
# -------------------------------------------

# Expose port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

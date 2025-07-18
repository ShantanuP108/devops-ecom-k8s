# Stage 1: Build the application with full dependencies
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src .

# Stage 2: Create the final, smaller production image
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# --- ADD THIS LINE ---
# Copy executable files like uvicorn from the builder stage
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

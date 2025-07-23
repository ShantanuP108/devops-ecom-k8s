from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI(title="Product Service")

@app.get("/")
def read_root():
    """A simple root endpoint that returns a welcome message."""
    return {"service": "Product Service", "status": "ok"}

# Triggering a new build

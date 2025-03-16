from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import socket  # To get the public hostname

from stock_market_analysis import generate_stock_charts

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend connection (Update to your frontend domain later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the public hostname (important for Render or any hosting service)
hostname = os.getenv("RENDER_EXTERNAL_URL", f"http://{socket.gethostname()}:8000")

@app.get("/")
def home():
    """Health check endpoint"""
    return {"message": "FastAPI Backend is Live!"}

@app.get("/stock/{ticker}")
def generate_stock_charts_api(ticker: str):
    """Generate stock charts for any stock ticker"""
    image_paths = generate_stock_charts(ticker)
    
    if isinstance(image_paths, dict):  # If error
        return JSONResponse(image_paths)

    # ✅ Fix: Use the correct base URL for images
    image_urls = [f"{hostname}/images/{os.path.basename(path)}" for path in image_paths]

    print(f"Generated images: {image_urls}")  # Debugging

    return JSONResponse({"images": image_urls})

# Serve static images
app.mount("/images", StaticFiles(directory="images"), name="images")


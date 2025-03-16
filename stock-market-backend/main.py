from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from stock_market_analysis import generate_stock_charts

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend connection
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stock/{ticker}")
def generate_stock_charts_api(ticker: str):
    """Generate stock charts for any stock ticker"""
    image_paths = generate_stock_charts(ticker)
    if isinstance(image_paths, dict):  # If error
        return JSONResponse(image_paths)

    image_urls = [f"http://127.0.0.1:8000/{path}" for path in image_paths]
    return JSONResponse({"images": image_urls})

# Serve static images
app.mount("/images", StaticFiles(directory="images"), name="images")


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from stock_market_analysis import generate_stock_charts

app = FastAPI()

# ✅ Correct CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # ✅ Local development (Vite)
        "http://localhost:3000",  # ✅ Local development (Create React App)
        "https://stockmarketanalysis.up.railway.app"  # ✅ Deployed frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Manually set the backend URL (DO NOT use socket.gethostname())
BACKEND_URL = "https://stock-market-analysis-production.up.railway.app"

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

    # ✅ Corrected image URLs
    image_urls = [f"{BACKEND_URL}/images/{os.path.basename(path)}" for path in image_paths]

    print(f"Generated images: {image_urls}")  # Debugging

    return JSONResponse({"images": image_urls})

# Serve static images
app.mount("/images", StaticFiles(directory="images"), name="images")

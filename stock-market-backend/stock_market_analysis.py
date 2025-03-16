# Future Imports must come first
from __future__ import division  

# Standard Library Imports
from datetime import datetime, timedelta  
import os
import logging

# Data Processing
import numpy as np
import pandas as pd
import yfinance as yf

# Data Visualization
import matplotlib
matplotlib.use("Agg")  # Prevent GUI errors in FastAPI
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure images directory exists
IMAGE_DIR = "images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def generate_stock_charts(ticker):
    """Fetch stock data, generate plots, and return saved image paths"""
    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)

    logger.info(f"Fetching stock data for {ticker} from {start} to {end}")
    stock_data = yf.download(ticker, start=start, end=end)

    if stock_data.empty or 'Close' not in stock_data.columns:
        logger.warning(f"No valid stock data found for {ticker}")
        return {"error": f"No data found for {ticker}"}

    image_paths = []

    # Plot Closing Price
    plt.figure(figsize=(10, 4))
    stock_data['Close'].plot(title=f"{ticker} Closing Price", legend=True)
    image_path = f"{IMAGE_DIR}/{ticker}_close.png"
    plt.savefig(image_path)
    plt.close()
    image_paths.append(image_path)

    # Plot Trading Volume
    plt.figure(figsize=(10, 4))
    stock_data['Volume'].plot(title=f"{ticker} Trading Volume", legend=True)
    image_path = f"{IMAGE_DIR}/{ticker}_volume.png"
    plt.savefig(image_path)
    plt.close()
    image_paths.append(image_path)

    # Compute Moving Averages
    MA_days = [10, 20, 50, 100]
    for ma in MA_days:
        stock_data[f"MA {ma}"] = stock_data['Close'].rolling(ma).mean()

    plt.figure(figsize=(10, 4))
    stock_data[['Close', 'MA 10', 'MA 20', 'MA 50', 'MA 100']].plot()
    plt.title(f"{ticker} Closing Price with Moving Averages")
    image_path = f"{IMAGE_DIR}/{ticker}_moving_avg.png"
    plt.savefig(image_path)
    plt.close()
    image_paths.append(image_path)

    # Plot Daily Return Histogram
    stock_data["Daily Return"] = stock_data["Close"].pct_change()
    sns.histplot(stock_data["Daily Return"].dropna(), bins=100, color="magenta", kde=True)
    plt.title(f"{ticker} Daily Return Histogram")
    image_path = f"{IMAGE_DIR}/{ticker}_daily_return.png"
    plt.savefig(image_path)
    plt.close()
    image_paths.append(image_path)

    # Monte Carlo Simulation
    try:
        start_price = float(stock_data['Close'].dropna().iloc[-1])  # Fix for float conversion issue
    except IndexError:
        logger.error("No closing price data available for Monte Carlo simulation.")
        return {"error": f"No valid closing price found for {ticker}"}

    days = 365
    mu = stock_data["Daily Return"].mean()
    sigma = stock_data["Daily Return"].std()

    logger.info(f"Running Monte Carlo simulation for {ticker} (mu={mu:.6f}, sigma={sigma:.6f})")

    plt.figure(figsize=(10, 5))
    for run in range(100):
        plt.plot(stock_monte_carlo(start_price, days, mu, sigma))
    plt.title(f"Monte Carlo Simulation for {ticker} Stock Price")
    plt.xlabel("Days")
    plt.ylabel("Price")
    image_path = f"{IMAGE_DIR}/{ticker}_monte_carlo.png"
    plt.savefig(image_path)
    plt.close()
    image_paths.append(image_path)

    # Next 7-Day Prediction (Monte Carlo)
    next_week_prices = stock_monte_carlo(start_price, 7, mu, sigma)

    plt.figure(figsize=(10, 4))
    plt.plot(range(1, 8), next_week_prices, marker="o", linestyle="dashed")
    plt.title(f"Next 7 Days Prediction for {ticker}")
    plt.xlabel("Days Ahead")
    plt.ylabel("Predicted Price")
    image_path = f"{IMAGE_DIR}/{ticker}_7day_prediction.png"
    plt.savefig(image_path)
    plt.close()
    image_paths.append(image_path)

    logger.info(f"Charts saved for {ticker}")

    return image_paths  # Return list of image paths


def stock_monte_carlo(start_price, days, mu, sigma):
    """Simulates stock prices using Geometric Brownian Motion"""
    price = np.zeros(days)
    price[0] = start_price
    shocks = np.random.normal(loc=mu / days, scale=sigma * np.sqrt(1 / days), size=days - 1)  # Fix size mismatch
    drifts = np.full(days - 1, mu / days)
    price[1:] = price[:-1] * (1 + drifts + shocks)
    return price

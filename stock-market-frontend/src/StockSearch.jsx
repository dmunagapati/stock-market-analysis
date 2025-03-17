import React from "react";
import { useState } from "react";
import axios from "axios";

function StockSearch({ setImages }) {
  const [ticker, setTicker] = useState("");

  const fetchCharts = async () => {
    try {
      const capitalizedTicker = ticker.toUpperCase().trim(); // Convert input to uppercase
      if (!ticker) return;
      console.log(`Fetching stock charts for: ${capitalizedTicker}`);

      const API_URL = "https://stock-market-analysis-production.up.railway.app/stock/";

      const response = await axios.get(`${API_URL}${capitalizedTicker}`);
      console.log("API Response:", response.data);
      setImages(response.data.images);
    } catch (error) {
      console.error("Error fetching stock data:", error);
    }
  };

  return (
    <div className="search-container">
      <input
        type="text"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
        placeholder="Enter stock symbol"
        className="input-box"
      />
      <button onClick={fetchCharts} className="get-charts-button">
        Get Charts
      </button>
    </div>
  );
}

export default StockSearch;
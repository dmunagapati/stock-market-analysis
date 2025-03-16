import React from "react";
import { useState } from "react";
import axios from "axios";

function StockSearch({ setImages }) {
  const [ticker, setTicker] = useState("");

  const fetchCharts = async () => {
    try {
      console.log(`Fetching stock charts for: ${ticker}`);

      // Update this URL to your Railway backend
      const API_URL = "stock-market-analysis-production.up.railway.app";

      const response = await axios.get(`${API_URL}${ticker}`);
      console.log("API Response:", response.data);
      setImages(response.data.images); // Ensure state updates correctly
    } catch (error) {
      console.error("Error fetching stock data:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
        placeholder="Enter stock symbol"
      />
      <button onClick={fetchCharts}>Get Stock Charts</button>
    </div>
  );
}

export default StockSearch;

import React from "react";
import { useState } from "react";
import axios from "axios";

function StockSearch({ setImages }) {
  const [ticker, setTicker] = useState("");

  const fetchCharts = async () => {
    try {
      console.log(`Fetching stock charts for: ${ticker}`);
      const response = await axios.get(`http://127.0.0.1:8000/stock/${ticker}`);
      console.log("API Response:", response.data);
      setImages(response.data.images); // Make sure this updates state correctly
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

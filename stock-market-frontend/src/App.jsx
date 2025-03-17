// src/App.jsx
import React, { useState } from "react";
import StockSearch from "./StockSearch";
import StockCharts from "./StockCharts";
import StockAccuracy from "./StockAccuracy"; // Import the new StockAccuracy component
import "./App.css";

function App() {
  const [images, setImages] = useState([]);
  const [accuracy, setAccuracy] = useState({}); // New state to hold accuracy data
  console.log("Accuracy Prop:", accuracy);

  return (
    <div className="container">
      <h1 className="title">Stock Market Analysis</h1>
      <p className="subtitle">Get real-time stock insights with interactive charts</p>
      <StockSearch setImages={setImages} setAccuracy={setAccuracy} />
      <StockCharts images={images} />
      <StockAccuracy accuracy={accuracy} />
    </div>
  );
}

export default App;

import React from "react";
import { useState } from "react";
import StockSearch from "./StockSearch";
import StockCharts from "./StockCharts";
import "./App.css"; 




function App() {
  const [images, setImages] = useState([]);

  return (
    <div className="container">
      <h1 className="title">Stock Market Analysis</h1>
      <p className="subtitle">Get real-time stock insights with interactive charts</p>
      <StockSearch setImages={setImages} />
      <StockCharts images={images} />
    </div>
  );
}

export default App;
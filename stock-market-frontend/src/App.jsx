import React from "react";
import { useState } from "react";
import StockSearch from "./StockSearch";
import StockCharts from "./StockCharts";



function App() {
  const [images, setImages] = useState([]);

  return (
    <div className="container">
      <h1>Stock Market Analysis</h1>
      <StockSearch setImages={setImages} />
      <StockCharts images={images} />
    </div>
  );
}

export default App;

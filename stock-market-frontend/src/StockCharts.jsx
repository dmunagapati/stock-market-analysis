import React from "react";

function StockCharts({ images }) {

  console.log("Images in StockCharts:", images);  // Log the images array to check if it has 7 items

  if (!images.length) {
    return <p style={{ color: "#34568B" }}>Enter a stock symbol to view data.</p>;
  }

  return (
    <div className="stock-charts">
      {images.map((src, index) => (
        <img key={index} src={src} alt={`Stock Chart ${index + 1}`} />
      ))}
    </div>
  );
}

export default StockCharts;

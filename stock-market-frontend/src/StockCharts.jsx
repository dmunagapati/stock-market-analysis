import React from "react";

function StockCharts({ images }) {
  console.log("Rendering images:", images);

  return (
    <div>
      {images.length === 0 ? (
        <p>No charts to display</p>
      ) : (
        images.map((img, index) => (
          <img key={index} src={img} alt={`Stock chart ${index}`} style={{ width: "600px", margin: "10px" }} />
        ))
      )}
    </div>
  );
}

export default StockCharts;
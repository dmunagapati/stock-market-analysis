import React from "react";

function StockAccuracy({ accuracy }) {
  // Check if accuracy data exists
  if (!accuracy) {
    return null; // If no accuracy data is available, render nothing
  }

  // If there's an error with accuracy
  if (accuracy.error) {
    return (
      <div className="accuracy">
        <p>{accuracy.error}</p>
      </div>
    );
  }

  // If accuracy data is available, render MAPE and RMSE
  return (
    <div className="accuracy">
      <h2>Prediction Accuracy</h2>
      <p><strong>MAPE:</strong> {accuracy.mape}%</p>
      <p><strong>RMSE:</strong> {accuracy.rmse}</p>
    </div>
  );
}

export default StockAccuracy;

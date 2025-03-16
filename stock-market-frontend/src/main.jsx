import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./style.css"; // Ensure this exists

const rootElement = document.getElementById("root");

if (!rootElement) {
  console.error("Root element not found! Make sure index.html has a <div id='root'>.");
} else {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}

import streamlit as st
import os

# Set Streamlit page layout
st.set_page_config(page_title="Stock Prediction Viewer", layout="wide")

# Title
st.title("📊 Stock Prediction Results Using LSTM")

# Sidebar instructions
st.sidebar.write("### Select a Stock to View its Predictions")

# Get available graphs
graph_folder = "graphs"
available_tickers = [
    f.replace("_accuracy.png", "").replace(".png", "").replace("_rmse.txt", "")
    for f in os.listdir(graph_folder) if f.endswith(".png")
]
available_tickers = list(set(available_tickers))  # Remove duplicates

# Dropdown to select stock ticker
selected_ticker = st.sidebar.selectbox("Choose a Stock:", available_tickers)

if selected_ticker:
    # Display RMSE Value
    rmse_file_path = f"{graph_folder}/{selected_ticker}_rmse.txt"
    if os.path.exists(rmse_file_path):
        with open(rmse_file_path, "r") as f:
            rmse_value = f.read().strip()
        st.sidebar.write(f"**Model RMSE:** {rmse_value} (Lower is better)")

    # Use columns to display graphs side by side
    col1, col2 = st.columns(2)

    # Show Forecast Graph in the first column
    forecast_path = f"{graph_folder}/{selected_ticker}.png"
    if os.path.exists(forecast_path):
        with col1:
            st.image(forecast_path, caption=f"Stock Price Prediction for {selected_ticker}", use_container_width=True)
    else:
        col1.warning(f"Forecast graph for {selected_ticker} not found.")

    # Show Accuracy Graph in the second column
    accuracy_path = f"{graph_folder}/{selected_ticker}_accuracy.png"
    if os.path.exists(accuracy_path):
        with col2:
            st.image(accuracy_path, caption=f"Model Accuracy for {selected_ticker}", use_container_width=True)
    else:
        col2.warning(f"Accuracy graph for {selected_ticker} not found.")
else:
    st.write("No predictions available yet. Run the notebook to generate graphs.")

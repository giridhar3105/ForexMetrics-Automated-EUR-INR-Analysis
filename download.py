import yfinance as yf

# Define the ticker symbol and date range
ticker_symbol = "EURINR=X"
start_date = "2023-01-01"
end_date = "2024-09-30"

# Download the data
currency_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save to CSV file
currency_data.to_csv("EUR_INR_data.csv")

print("Data saved to EUR_INR_data.csv")

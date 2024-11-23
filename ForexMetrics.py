import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ================================
# SECTION 1: Download Dataset
# ================================
print("========== Downloading EUR/INR dataset ==============")
eur_inr_data = yf.download('EURINR=X', start='2023-01-01', end='2024-09-30')
print("Columns in data:", eur_inr_data.columns)

# Ensure data contains the expected columns
required_columns = {('Close', 'EURINR=X'), ('High', 'EURINR=X'), ('Low', 'EURINR=X')}
if not required_columns.issubset(eur_inr_data.columns):
    raise KeyError("Data does not contain 'Close', 'High', or 'Low' columns. Please check data source.")

# ================================
# SECTION 2: Calculate Technical Indicators
# ================================
print("========== Calculating Technical Indicators ==============")
# Moving Averages: Simple and Exponential
eur_inr_data['20_SMA'] = eur_inr_data[('Close', 'EURINR=X')].rolling(window=20).mean()
eur_inr_data['50_SMA'] = eur_inr_data[('Close', 'EURINR=X')].rolling(window=50).mean()
eur_inr_data['10_EMA'] = eur_inr_data[('Close', 'EURINR=X')].ewm(span=10, adjust=False).mean()

# Bollinger Bands
eur_inr_data['20_day_MA'] = eur_inr_data[('Close', 'EURINR=X')].rolling(window=20).mean()
eur_inr_data['20_day_std'] = eur_inr_data[('Close', 'EURINR=X')].rolling(window=20).std()
eur_inr_data['Upper_Band'] = eur_inr_data['20_day_MA'] + (eur_inr_data['20_day_std'] * 2)
eur_inr_data['Lower_Band'] = eur_inr_data['20_day_MA'] - (eur_inr_data['20_day_std'] * 2)
eur_inr_data['BB_width'] = eur_inr_data['Upper_Band'] - eur_inr_data['Lower_Band']

# Commodity Channel Index (CCI) - 20-day and 50-day
eur_inr_data['TP'] = (eur_inr_data[('High', 'EURINR=X')] + 
                      eur_inr_data[('Low', 'EURINR=X')] + 
                      eur_inr_data[('Close', 'EURINR=X')]) / 3

# Calculate Mean Absolute Deviation manually within the rolling window
def mean_absolute_deviation(series):
    return np.mean(np.abs(series - series.mean()))

eur_inr_data['CCI_20'] = (eur_inr_data['TP'] - eur_inr_data['TP'].rolling(20).mean()) / \
                         (0.015 * eur_inr_data['TP'].rolling(20).apply(mean_absolute_deviation, raw=True))
eur_inr_data['CCI_50'] = (eur_inr_data['TP'] - eur_inr_data['TP'].rolling(50).mean()) / \
                         (0.015 * eur_inr_data['TP'].rolling(50).apply(mean_absolute_deviation, raw=True))

# Relative Strength Index (RSI) - 14-day
delta = eur_inr_data[('Close', 'EURINR=X')].diff(1)
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
eur_inr_data['RSI'] = 100 - (100 / (1 + rs))

# Fill any remaining NaN values to avoid issues with missing data
eur_inr_data = eur_inr_data.ffill().bfill()

# ================================
# SECTION 3: Extract Latest Data
# ================================
print("========== Extracting Latest Data ==============")
latest_data = eur_inr_data.iloc[-1]

# ================================
# SECTION 4: Decision-Making Logic
# ================================
print("========== Making Trading Decision ==============")
decision = "UNKNOWN"  # Initialize decision variable

try:
    close_price = latest_data[('Close', 'EURINR=X')]
    
    # Extract indicator values as scalars
    ten_ema = latest_data['10_EMA'].item()  # Use .item() to get the scalar value
    twenty_sma = latest_data['20_SMA'].item()  # Use .item() to get the scalar value
    cci_20 = latest_data['CCI_20'].item()  # Use .item() to get the scalar value
    rsi = latest_data['RSI'].item()  # Use .item() to get the scalar value
    lower_band = latest_data['Lower_Band'].item()  # Use .item() to get the scalar value
    upper_band = latest_data['Upper_Band'].item()  # Use .item() to get the scalar value
    bb_width_mean = eur_inr_data['BB_width'].mean()

    # Boolean conditions
    condition_buy = (
        close_price > ten_ema and
        close_price > twenty_sma and
        cci_20 < -100 and
        rsi < 30 and
        close_price <= lower_band and
        latest_data['BB_width'] > bb_width_mean
    )

    condition_sell = (
        close_price < ten_ema and
        close_price < twenty_sma and
        cci_20 > 100 and
        rsi > 70 and
        close_price >= upper_band and
        latest_data['BB_width'] > bb_width_mean
    )

    # Determine decision
    if condition_buy:
        decision = 'BUY'
    elif condition_sell:
        decision = 'SELL'
    else:
        decision = 'NEUTRAL'
        
except KeyError as e:
    print(f"KeyError: {e}. Please check that all indicators are computed correctly.")
except ValueError as ve:
    print(f"ValueError: {ve}. This might be due to ambiguous truth values in conditions.")

# ================================
# SECTION 5: Output Results
# ================================
print("========== Technical Indicators on the Last Date ==============")
print(f"Close Price: {latest_data[('Close', 'EURINR=X')]}")
print(f"20-SMA: {latest_data['20_SMA']}")
print(f"50-SMA: {latest_data['50_SMA']}")
print(f"10-EMA: {latest_data['10_EMA']}")
print(f"Bollinger Upper Band: {latest_data['Upper_Band']}")
print(f"Bollinger Lower Band: {latest_data['Lower_Band']}")
print(f"Bollinger Band Width: {latest_data['BB_width']}")
print(f"CCI 20-day: {latest_data['CCI_20']}")
print(f"CCI 50-day: {latest_data['CCI_50']}")
print(f"RSI: {latest_data['RSI']}")
print(f"Decision: {decision}")

# ================================
# SECTION 6: Visualization
# ================================
print("========== Generating Visualizations ==============")

# Plot Close Price with Moving Averages
plt.figure(figsize=(14, 8))
plt.plot(eur_inr_data.index, eur_inr_data[('Close', 'EURINR=X')], label='Close Price', color='black')
plt.plot(eur_inr_data.index, eur_inr_data['20_SMA'], label='20-SMA', color='blue', linestyle='--')
plt.plot(eur_inr_data.index, eur_inr_data['50_SMA'], label='50-SMA', color='red', linestyle='--')
plt.plot(eur_inr_data.index, eur_inr_data['10_EMA'], label='10-EMA', color='green', linestyle='--')
plt.title('EUR/INR Close Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.show()

# Plot Bollinger Bands
plt.figure(figsize=(14, 8))
plt.plot(eur_inr_data.index, eur_inr_data[('Close', 'EURINR=X')], label='Close Price', color='black')
plt.plot(eur_inr_data.index, eur_inr_data['Upper_Band'], label='Upper Bollinger Band', color='blue', linestyle='--')
plt.plot(eur_inr_data.index, eur_inr_data['Lower_Band'], label='Lower Bollinger Band', color='red', linestyle='--')
plt.fill_between(eur_inr_data.index, eur_inr_data['Lower_Band'], eur_inr_data['Upper_Band'], color='gray', alpha=0.3)
plt.title('EUR/INR Close Price with Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.show()

# Plot RSI
plt.figure(figsize=(14, 6))
plt.plot(eur_inr_data.index, eur_inr_data['RSI'], label='RSI', color='purple')
plt.axhline(70, linestyle='--', color='red', alpha=0.5, label='Overbought (70)')
plt.axhline(30, linestyle='--', color='green', alpha=0.5, label='Oversold (30)')
plt.title('EUR/INR Relative Strength Index (RSI)')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend(loc='best')
plt.show()

# Plot CCI
plt.figure(figsize=(14, 6))
plt.plot(eur_inr_data.index, eur_inr_data['CCI_20'], label='CCI 20-day', color='blue')
plt.plot(eur_inr_data.index, eur_inr_data['CCI_50'], label='CCI 50-day', color='orange')
plt.axhline(100, linestyle='--', color='red', alpha=0.5, label='Overbought (100)')
plt.axhline(-100, linestyle='--', color='green', alpha=0.5, label='Oversold (-100)')
plt.title('EUR/INR Commodity Channel Index (CCI)')
plt.xlabel('Date')
plt.ylabel('CCI')
plt.legend(loc='best')
plt.show()

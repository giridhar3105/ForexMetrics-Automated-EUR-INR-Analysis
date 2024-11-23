# ForexMetrics: Automated EUR/INR Analysis

ForexMetrics is a Python-based project that automates technical analysis of the EUR/INR currency pair. Using real-time data from Yahoo Finance, it calculates key technical indicators, provides actionable trading decisions, and generates visualizations for deeper market insights.

## Features
1. **Automated Data Fetching**:
   - Retrieves historical EUR/INR data from Yahoo Finance for a specified time period.

2. **Technical Indicators**:
   - **Moving Averages**:
     - 20-day Simple Moving Average (SMA)
     - 50-day Simple Moving Average (SMA)
     - 10-day Exponential Moving Average (EMA)
   - **Bollinger Bands**:
     - Upper Band, Lower Band, and Bandwidth
   - **Commodity Channel Index (CCI)**:
     - 20-day and 50-day values
   - **Relative Strength Index (RSI)**:
     - 14-day values

3. **Decision-Making**:
   - Determines Buy, Sell, or Neutral signals based on a combination of indicators.
   - Evaluates the latest market conditions for actionable insights.

4. **Visualizations**:
   - Generates plots for close price trends, Bollinger Bands, RSI, and CCI to visually interpret market movements.

## Goals of the Project
1. Automate the technical analysis of the EUR/INR currency pair for consistent and accurate insights.
2. Provide easy-to-interpret trading recommendations based on market data.
3. Enhance user understanding through detailed visualizations.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ForexMetrics.git
   cd ForexMetrics

## Usage
1. Run the script:
   ```bash
   python ForexMetrics.py
   ```
2. The script will:
   - Fetch historical EUR/INR data.
   - Calculate technical indicators.
   - Display trading decisions and key metrics.
   - Generate and show visual plots for analysis.

## Process (Summary)
1. Download EUR/INR currency data from Yahoo Finance for a specified date range.
2. Compute technical indicators (Moving Averages, Bollinger Bands, RSI, and CCI).
3. Analyze the latest market data to suggest trading actions (Buy, Sell, Neutral).
4. Visualize data trends for better market interpretation.

## Example Output
```
========== Technical Indicators on the Last Date ============
Close Price: 88.235
20-SMA: 87.954
50-SMA: 87.650
10-EMA: 88.145
Bollinger Upper Band: 89.320
Bollinger Lower Band: 86.588
Bollinger Band Width: 2.732
CCI 20-day: -120.34
CCI 50-day: -80.21
RSI: 28.56
Decision: BUY
```

## Visualizations
- **Close Price with Moving Averages**  
- **Bollinger Bands**  
- **RSI with Overbought/Oversold Levels**  
- **CCI with Thresholds**  

## Prerequisites
- Python 3.7 or later
- Libraries: `yfinance`, `pandas`, `numpy`, `matplotlib`

## Contributing
Contributions are welcome! If you have ideas for improving the tool, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Developed by [Chennuru Giridhar](https://github.com/giridhar3105).
```

This README is concise, clear, and ready for GitHub. Update the repository link (`yourusername`) and include a `LICENSE` file if needed. Let me know if you need further changes!

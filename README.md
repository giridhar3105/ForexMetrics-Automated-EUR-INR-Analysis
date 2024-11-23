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

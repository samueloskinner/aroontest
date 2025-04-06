import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_stock_data(tickers, period="1y"):
    """
    Fetch stock data using yfinance
    Args:
        tickers (list): List of stock ticker symbols
        period (str): Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    Returns:
        dict: Dictionary of pandas DataFrames with stock data
    """
    stock_data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            stock_data[ticker] = stock.history(period=period)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return stock_data

def calculate_aroon(data, period=14):
    """
    Calculate Aroon indicators
    Args:
        data (pd.DataFrame): DataFrame with 'High' and 'Low' columns
        period (int): Looking back period
    Returns:
        tuple: (Aroon Up, Aroon Down)
    Raises:
        ValueError: If required columns are missing
    """
    if 'High' not in data.columns or 'Low' not in data.columns:
        raise ValueError("DataFrame must contain 'High' and 'Low' columns")
    
    if period <= 0:
        raise ValueError("Period must be positive")
        
    aroon_up = 100 * (period - data['High'].rolling(window=period).apply(lambda x: period - 1 - x.argmax())) / period
    aroon_down = 100 * (period - data['Low'].rolling(window=period).apply(lambda x: period - 1 - x.argmin())) / period
    return aroon_up, aroon_down

def main(tickers, period="1y"):
    stock_data = fetch_stock_data(tickers, period)
    results = {}
    
    for ticker, data in stock_data.items():
        if not data.empty:
            aroon_up, aroon_down = calculate_aroon(data)
            results[ticker] = {
                'aroon_up': aroon_up.iloc[-1],
                'aroon_down': aroon_down.iloc[-1],
                'last_date': data.index[-1].strftime('%Y-%m-%d')
            }
            print(f"\nAroon Indicator for {ticker} as of {results[ticker]['last_date']}:")
            print("Aroon Up:", results[ticker]['aroon_up'])
            print("Aroon Down:", results[ticker]['aroon_down'])

if __name__ == "__main__":
    tickers = ['AAPL', 'GOOGL', 'MSFT']  # Example tickers
    main(tickers)
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

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

def plot_aroon_indicators(data, aroon_up, aroon_down, ticker):
    """Plot Aroon indicators with stock price and signals."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [2, 1]})
    
    # Plot stock price
    ax1.plot(data.index, data['Close'], label='Close Price', color='black')
    ax1.set_title(f'{ticker} Stock Price and Aroon Indicators')
    ax1.grid(True)
    ax1.legend()
    
    # Plot Aroon indicators
    ax2.plot(aroon_up.index, aroon_up, label='Aroon Up', color='green')
    ax2.plot(aroon_down.index, aroon_down, label='Aroon Down', color='red')
    ax2.axhline(y=70, color='grey', linestyle='--', alpha=0.5)
    ax2.axhline(y=30, color='grey', linestyle='--', alpha=0.5)
    ax2.set_ylim(-5, 105)
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    return fig

def analyze_aroon_signals(aroon_up, aroon_down):
    """Analyze Aroon indicators and generate trading signals."""
    signals = []
    
    # Latest values
    last_up = aroon_up.iloc[-1]
    last_down = aroon_down.iloc[-1]
    
    # Strong trend signals
    if last_up > 70 and last_down < 30:
        signals.append("STRONG UPTREND: Consider long positions")
    elif last_down > 70 and last_up < 30:
        signals.append("STRONG DOWNTREND: Consider short positions")
        
    # Crossover signals
    if aroon_up.iloc[-2] < aroon_down.iloc[-2] and last_up > last_down:
        signals.append("BULLISH CROSSOVER: Potential buying opportunity")
    elif aroon_up.iloc[-2] > aroon_down.iloc[-2] and last_up < last_down:
        signals.append("BEARISH CROSSOVER: Potential selling opportunity")
        
    # No clear trend
    if 30 <= last_up <= 70 and 30 <= last_down <= 70:
        signals.append("NO CLEAR TREND: Market in consolidation")
        
    return signals

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
            
            # Plot Aroon indicators
            fig = plot_aroon_indicators(data, aroon_up, aroon_down, ticker)
            plt.show()
            
            # Analyze Aroon signals
            signals = analyze_aroon_signals(aroon_up, aroon_down)
            for signal in signals:
                print(signal)

if __name__ == "__main__":
    tickers = ['AAPL', 'GOOGL', 'MSFT']  # Example tickers
    main(tickers)
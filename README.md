# README.md

# Stock Data Aroon Indicator

This Python package retrieves the latest stock data for a set of specified tickers and calculates the Aroon indicator, which is a technical analysis tool used to measure the strength of a trend.

## Installation

To install the package, you can use pip:

```bash
pip install .
```

## Usage

To use the package, you can import the main module and call the relevant functions. Here is a simple example:

```python
import aroontest
from aroontest.main import (
    fetch_stock_data, 
    calculate_aroon, 
    plot_aroon_indicators, 
    analyze_aroon_signals
)

# Fetch data and calculate indicators
ticker = 'AAPL'
tickers = [ticker]
data = fetch_stock_data(tickers)
stock_data = data[ticker]
aroon_up, aroon_down = calculate_aroon(stock_data)

# Plot the indicators
fig = plot_aroon_indicators(stock_data, aroon_up, aroon_down, ticker)
fig.show()

# Get trading signals
signals = analyze_aroon_signals(aroon_up, aroon_down)
for signal in signals:
    print(signal)
```

The Aroon indicators help identify trend strength and potential reversals:
- Aroon-Up > 70: Strong uptrend
- Aroon-Down > 70: Strong downtrend
- Crossovers between Aroon-Up and Aroon-Down can signal potential trend changes
- Both indicators between 30-70 suggest consolidation/no clear trend

## AI-Powered Analysis

The package includes modern AI agents for advanced analysis:

```python
import asyncio
from aroontest import AroonAnalyst

async def main():
    # Initialize the analysis system
    analyst = AroonAnalyst()
    
    # Perform comprehensive analysis
    analysis = await analyst.analyze_stock('AAPL')
    print("Analysis Results:", analysis)
    
    # Optimize trading strategy
    strategy = await analyst.optimize_strategy('AAPL')
    print("Strategy Optimization:", strategy)

# Run the analysis
asyncio.run(main())
```

Key features of the AI system:
- Multi-agent collaboration using GroupChat
- Asynchronous processing
- Cross-validated strategy optimization
- Detailed visualization and reporting

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
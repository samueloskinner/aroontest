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
from aroontest.main import fetch_stock_data, calculate_aroon

tickers = ['AAPL', 'GOOGL', 'MSFT']
data = fetch_stock_data(tickers)
aroon_up, aroon_down = calculate_aroon(data['AAPL'])
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
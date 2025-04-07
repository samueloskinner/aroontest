# File: /python-package/python-package/src/__init__.py

"""
This package provides functionality to pull the latest stock data for specified tickers
and calculate the Aroon indicator.
"""

from .main import (
    fetch_stock_data,
    calculate_aroon,
    plot_aroon_indicators,
    analyze_aroon_signals
)
from .agents import AroonAnalyst

__version__ = "0.2.0"

__all__ = [
    'AroonAnalyst',
    'fetch_stock_data',
    'calculate_aroon',
    'plot_aroon_indicators',
    'analyze_aroon_signals',
]
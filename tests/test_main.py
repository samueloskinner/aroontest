import unittest
import pandas as pd
import numpy as np
from aroontest.main import fetch_stock_data, calculate_aroon

class TestMain(unittest.TestCase):

    def test_fetch_stock_data(self):
        tickers = ['AAPL', 'GOOGL']
        data = fetch_stock_data(tickers)
        self.assertIsInstance(data, dict)
        self.assertIn('AAPL', data)
        self.assertIn('GOOGL', data)

    def test_calculate_aroon(self):
        # Create sample DataFrame with High and Low columns
        dates = pd.date_range(start='2024-01-01', periods=10)
        sample_data = pd.DataFrame({
            'High': [22, 23, 21, 24, 25, 20, 19, 22, 23, 21],
            'Low': [20, 21, 19, 22, 23, 18, 17, 20, 21, 19]
        }, index=dates)
        
        aroon_up, aroon_down = calculate_aroon(sample_data)
        self.assertIsInstance(aroon_up, pd.Series)
        self.assertIsInstance(aroon_down, pd.Series)

if __name__ == '__main__':
    unittest.main()
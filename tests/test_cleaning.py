import unittest
import pandas as pd
from cleanpipe.cleaning import drop_missing, fill_missing, convert_dtype, rename_columns, CleanPipe

class TestCleaning(unittest.TestCase):
    def test_drop_missing(self):
        data = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        cleaned_data = drop_missing(data)
        self.assertEqual(len(cleaned_data), 1)

    def test_fill_missing(self):
        data = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        filled_data = fill_missing(data, 0)
        self.assertTrue(filled_data.isna().sum().sum() == 0)

    # Add more test cases for other functions and the CleanPipe class

if __name__ == '__main__':
    unittest.main()
import unittest
import pandas as pd
import numpy as np
from cleanpipe.cleaning import (
    drop_missing,
    fill_missing,
    convert_dtype,
    rename_columns,
    remove_duplicates,
    remove_outliers,
    standardize_date_format,
    encode_categorical,
    scale_features,
    impute_missing,
    CleanPipe
)

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing."""
        self.df = pd.DataFrame({
            'A': [1, 2, np.nan, 4, 5],
            'B': ['a', 'b', 'b', np.nan, 'e'],
            'C': [10, 11, 12, 13, 14],
            'D': ['2025-01-01', '2025-01-02', np.nan, '2025-01-04', '2025-01-05']
        })

    def test_drop_missing(self):
        """Test dropping rows with missing values."""
        result = drop_missing(self.df)
        self.assertEqual(result.shape[0], 3)

    def test_fill_missing(self):
        """Test filling missing values."""
        result = fill_missing(self.df, value=0)
        self.assertEqual(result.isnull().sum().sum(), 0)

    def test_convert_dtype(self):
        """Test converting data type of a column."""
        result = convert_dtype(self.df, 'A', 'str')
        self.assertEqual(result['A'].dtype, object)

    def test_rename_columns(self):
        """Test renaming columns."""
        result = rename_columns(self.df, {'A': 'Alpha', 'B': 'Beta'})
        self.assertIn('Alpha', result.columns)
        self.assertIn('Beta', result.columns)

    def test_remove_duplicates(self):
        """Test removing duplicate rows."""
        df = pd.concat([self.df, pd.DataFrame([self.df.iloc[0]])], ignore_index=True)
        result = remove_duplicates(df)
        self.assertEqual(result.shape[0], self.df.shape[0])

    def test_remove_outliers(self):
        """Test removing outliers."""
        df = self.df.copy()
        df.loc[0, 'C'] = 100  # Introduce an outlier
        result = remove_outliers(df, ['C'])
        self.assertEqual(result.shape[0], self.df.shape[0] - 1)

    def test_standardize_date_format(self):
        """Test standardizing date format."""
        result = standardize_date_format(self.df, 'D')
        self.assertEqual(result['D'].iloc[0], '2025-01-01')

    def test_encode_categorical(self):
        """Test one-hot encoding of categorical variables."""
        result = encode_categorical(self.df, ['B'])
        self.assertIn('B_a', result.columns)
        self.assertIn('B_b', result.columns)

    def test_scale_features(self):
        """Test scaling numerical features."""
        result = scale_features(self.df, ['C'])
        self.assertAlmostEqual(result['C'].mean(), 0, places=6)
        self.assertAlmostEqual(result['C'].std(ddof=0), 1, places=6)

    def test_impute_missing(self):
        """Test imputing missing values."""
        result = impute_missing(self.df, strategy='mean', columns=['A'])
        self.assertEqual(result['A'].isnull().sum(), 0)

    def test_cleanpipe_class(self):
        """Test the CleanPipe class."""
        cp = CleanPipe(self.df)
        result = cp.drop_missing().get_df()
        self.assertEqual(result.shape[0], 3)

if __name__ == '__main__':
    unittest.main()

def drop_missing(data):
    """Drop rows with missing values."""
    return data.dropna()

def fill_missing(data, value):
    """Fill missing values with a specified value."""
    return data.fillna(value)

def convert_dtype(data, dtype):
    """Convert columns to a specified data type."""
    return data.astype(dtype)

def rename_columns(data, columns):
    """Rename columns in the DataFrame."""
    data.columns = columns
    return data

class CleanPipe:
    """Pipeline for cleaning data."""
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self, data):
        for step in self.steps:
            data = step(data)
        return data
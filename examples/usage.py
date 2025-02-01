import pandas as pd
from cleanpipe.cleaning import CleanPipe

# Load your data
df = pd.read_csv("your_data.csv")

# Clean the data using a chainable API
cleaned_df = (CleanPipe(df)
              .drop_missing(axis=0)
              .rename_columns({'old_name': 'new_name'})
              .fill_missing(0)
              .get_df())

print(cleaned_df)

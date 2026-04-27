# Import the `pandas` library
import pandas as pd

# Read the csv file
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/IMDb_Data_final.csv')

# Extract data with even indices
even = data.iloc[lambda x: x.index % 2 == 0]
# Extract data with odd indices
odd = data.iloc[lambda x: x.index % 2 != 0]

# Output data
print(even.loc[0:5], odd.loc[-1:-6])
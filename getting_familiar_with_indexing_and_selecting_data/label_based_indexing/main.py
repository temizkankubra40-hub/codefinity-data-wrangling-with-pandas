# Import the `pandas` library
import pandas as pd

# Read the csv file
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/IMDb_Data_final.csv')

# Slice the data
data_extracted = data.loc[15:85, ['Title', 'Stars', 'Category']]

# Output the resulting dataset
print(data_extracted)
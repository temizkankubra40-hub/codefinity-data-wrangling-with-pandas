import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars.csv', index_col = 0)

# Apply the `.corr()` method
print(data.corr(numeric_only=True))
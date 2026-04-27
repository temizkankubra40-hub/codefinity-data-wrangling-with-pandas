import pandas as pd

data = pd.read_csv(
    'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet',
    index_col=0
)

# Extract data with both correct conditions
data_extracted = data.loc[
    (data['absolute_magnitude'] >= 25) &
    (data['hazardous'] == False)
]

# Output 5 random rows
print(data_extracted.sample(5))
import pandas as pd

data = pd.read_csv(
    'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic3.csv',
    index_col=0
)

# 1. Create dummy variables for 'Sex'
data = pd.get_dummies(data, columns=['Sex'])

# 2. Sum each dummy column
sex_male = data['Sex_male'].sum()
sex_female = data['Sex_female'].sum()

# 3. Output the result
print(sex_male, sex_female)
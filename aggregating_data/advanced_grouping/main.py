import pandas as pd
url = 'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane'
data = pd.read_csv(url, index_col=0)

# Store columns
columns = ['AirportFrom', 'Airline', 'DayOfWeek', 'Time', 'Length']

# Extract needed columns
data_subset = data[columns]

# Group and calculate minimum of (Length + Time)
data_flights = data_subset \
    .groupby(['AirportFrom', 'Airline', 'DayOfWeek']) \
    .apply(lambda x: (x['Length'] + x['Time']).min())


# Output
print(data_flights.head(10))

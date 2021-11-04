import pandas as pd

# Create data set.
dataSet = {'First Name': ['Jonny','Holly','Nira'],
           'Grade': [85,95,91] }

# Create dataframe with data set and named columns.
# Column names must match the dataSet properties.
df = pd.DataFrame(dataSet, columns= ['First Name', 'Grade'])

# Show DataFrame
print(df)

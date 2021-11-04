import pandas as pd

# Create data set.
dataSet = { 'Fahrenheit': [85,95,91] }

# Create dataframe with data set and named columns.
# Column names must match the dataSet properties.
df = pd.DataFrame(dataSet, columns= ['Fahrenheit'])
df['Celsius'] = (df['Fahrenheit']-32)*5/9
# Show DataFrame
print(df)
# Add the third col
df['Kelvin']=df['Celsius']+273.15
print(df)

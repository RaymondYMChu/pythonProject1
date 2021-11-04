import pandas as pd

# Create data set.
dataSet = { 'Fahrenheit': [85,95,91] }

# Create dataframe with data set and named columns.
# Column names must match the dataSet properties.
df = pd.DataFrame(dataSet, columns= ['Fahrenheit'])
df['Celsius'] = (df['Fahrenheit']-32)*5/9
# Show DataFrame
print(df)
for i in range(0, len(df)-1):
    celsius = (df.iloc[i]['Fahrenheit'] - 32)*/9
    df.iat[i, Celsius] = celsius
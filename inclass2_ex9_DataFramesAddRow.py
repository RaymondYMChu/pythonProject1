import pandas as pd

# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }
# Create dataframe with data set and named columns.
df1 = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
dataSet2 = { 'Market': ['Hang Seng', 'DAX'],
             'Last': [26918.58, 11872.44]}
df2 = pd.DataFrame(dataSet2, columns= ['Market', 'Last'])
df1 = df1.append(df2)
# Show original DataFrame.
print("\n*** Original DataFrame ***")
print(df1)

dataSet3 = { 'Market': ['FTSE100'],
             'Last': [7407.06]}
df3 = pd.DataFrame(dataSet3, columns= ['Market', 'Last'])
df1 = df1.append(df3)

print("\n*** Adjusted DataFrame ***")
print(df1)

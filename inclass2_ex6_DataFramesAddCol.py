import pandas as pd

# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }

# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])

# Show original DataFrame.
print("\n*** Original DataFrame ***")
print(df)

# Create change column.
change = [-21.51, -98.41, -453.83]

# Append change column.
df['Change'] = change

# Show revised DataFrame.
print("\n*** Adjusted DataFrame ***")
print (df)

# Create Percentage change column.
percentageChange = [-0.73, -0.37, -2.11]

# Append Percentage change column.
df['Percentage Change'] = percentageChange

# Show revised DataFrame.
print("\n*** Adjusted DataFrame with forth column ***")
print (df)
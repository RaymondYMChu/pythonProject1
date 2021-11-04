import pandas as pd

# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }

# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])

# Add new line.
print("\n")

# Show names only
print(df.loc[0]['Market'],df.loc[0]['Last'])


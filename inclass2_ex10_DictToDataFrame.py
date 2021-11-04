import pandas as pd

# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', ],
           'Last': [2932.05, 26485.01 ]}

# The dictionary is an object made of name value pairs.
stockDictionary = {'Market': 'Nikkei', 'Last': 21087.16 }

# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])

# Show original DataFrame.
print("\n*** Original DataFrame ***")

df = df.append(stockDictionary, ignore_index=True)
print(df);

# Create stockDictionary2
stockDictionary2 ={'Market':'DAX','Last':'11872.44'}
df=df.append(stockDictionary2, ignore_index=True)

# Show Adjusted DataFrame.
print("\n*** Adjusted DataFrame ***")
print(df);
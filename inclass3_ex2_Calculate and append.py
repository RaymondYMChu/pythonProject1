import pandas as pd

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_DATA="phone_data.csv"

df=pd.read_csv(PATH+CSV_DATA, header=1, encoding="ISO-8859-1",sep=',',
               names=('index','Date','duration','item','month','network','network_type'))
# Get count of items per month.
dfStats = df.groupby('network_type')['index'] \
    .count().reset_index().rename(columns={'index': '# Calls'})
# Get duration mean for network groups and convert to DataFrame.
dfDurationMean = df.groupby('network_type')['duration'] \
    .mean().reset_index().rename(columns={'duration': 'Duration Mean'})
# Get duration max for network groups and convert to DataFrame.
dfDurationMax = df.groupby('network_type')['duration'] \
    .max().reset_index().rename(columns={'duration':'Duration Max'})
dfDurationMin =df.groupby('network_type')['duration'] \
    .min().reset_index().rename(columns={'duration':'Duration Min'})
dfDurationStdv =df.groupby('network_type')['duration']\
    .std().reset_index().rename(columns={'duration':'Duration Stdv'})
# Append duration mean to stats matrix.
dfStats['Duration Mean'] = dfDurationMean['Duration Mean']
# Append duration max to stats matrix.
dfStats['Duration Max'] = dfDurationMax['Duration Max']
dfStats['Duration Min'] = dfDurationMin['Duration Min']
dfStats['Duration Stdv'] = dfDurationStdv['Duration Stdv']

print(dfStats)
import pandas as pd

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
FILE ="babysamp-98.txt"

df=pd.read_csv(PATH+FILE, skiprows=1, sep='\t', names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Get count of people by sex.
dfStats = df.groupby('sex')['weight'].count().reset_index().rename(columns={'weight': '# of people'})
dfWeightMean = df.groupby('sex')['weight'] \
    .mean().reset_index().rename(columns={'weight': 'Mean Weight'})
# Get duration max for network groups and convert to DataFrame.
dfWeightMax = df.groupby('sex')['weight'] \
    .max().reset_index().rename(columns={'weight':'Max Weight'})
dfWeightMin =df.groupby('sex')['weight'] \
    .min().reset_index().rename(columns={'weight':'Min Weight'})
# Append mean/max/min to stats matrix.
dfStats['Max Weight'] = dfWeightMax['Max Weight']
dfStats['Min Weight'] = dfWeightMin['Min Weight']
dfStats['Mean Weight'] = dfWeightMean['Mean Weight']

print(dfStats)
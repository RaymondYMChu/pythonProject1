import pandas as pd

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_DATA = "heart_original.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1, encoding="ISO-8859-1", sep=',',
                 names=('age', 'sex','cp','trestbps', 'chol','fbs',
                        'restecg','thalach','exang','oldpeak','slope','ca',
                        'thal','target'))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
dfStats = df.groupby('age')['chol'] \
    .count().reset_index().rename(columns={'chol': 'Total People'})
# Get duration mean for network groups and convert to DataFrame.
dfCholMean = df.groupby('age')['chol'] \
    .mean().reset_index().rename(columns={'chol': 'Mean Cholesterol Level'})
dfStats['Mean Cholesterol Level'] = dfCholMean['Mean Cholesterol Level']
#to rearrange col
dfStats3=dfStats[['age','Mean Cholesterol Level','Total People']]
print(dfStats3)

dfStats2 = dfStats[['age','Mean Cholesterol Level']]

#command below is used to avoid warning of using copy of dataframe is on
pd.options.mode.chained_assignment = None
dfStats2['age'] = 0
dfStats2['Mean Cholesterol Level'] = 0.0
age_idx = 0
mean_idx = 1

#Part 2 for loop to do filter
for i in range(0,len(dfStats)):
        age = (dfStats.iloc[i]['age'])
        mean = (dfStats.iloc[i]['Mean Cholesterol Level'])
        dfStats2.iat[i,age_idx] = age
        dfStats2.iat[i,mean_idx]= mean
print(dfStats2)
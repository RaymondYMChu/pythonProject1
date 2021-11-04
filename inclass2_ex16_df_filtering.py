import pandas as pd

# Import data into a DataFrame.
path = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Rename the columns so they are more reader-friendly.
df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method
# Show all columns.
pd.set_option('display.max_columns', None)
# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
print("Count:  "+str(df['Mom Age'].count()))
print("Min:  "+str(df['Mom Age'].min()))
print("Max:  "+str(df['Mom Age'].max()))
print("Mean:  "+str(df['Mom Age'].mean()))
print("Median:  "+str(df['Mom Age'].median()))
print("Standard Deviation:  "+str(df['Mom Age'].std()))
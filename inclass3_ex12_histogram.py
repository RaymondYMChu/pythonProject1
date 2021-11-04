import pandas as pd
import matplotlib.pyplot as plt

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
FILE ="babysamp-98.txt"

df=pd.read_csv(PATH+FILE, skiprows=1, sep='\t', names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

plt.hist(df["MomAge"], bins=22)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title('Mother Age')

plt.show()

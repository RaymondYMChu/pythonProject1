import pandas as pd
import matplotlib.pyplot as plt

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
FILE ="bodyfat.txt"

df = pd.read_csv(PATH+FILE, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))

# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
# This line allows us to set the figure size supposedly in inches.
# When rendered in the IDE the output often does not translate to inches.
plt.subplots(nrows=3, ncols=3,  figsize=(14,7))

plt.subplot(3, 3, 3) # Specfies total rows, columns and image #
                     # where images are drawn clockwise.
plt.hist(df["Pct.BF"], bins=10)
plt.xlabel("Pct.BF")
plt.ylabel("Freq")

plt.subplot(3, 3, 2) # Specfies total rows, columns and image #
                     # where images are drawn clockwise.
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.subplot(3, 3, 9) # Specfies total rows, columns and image #
                     # where images are drawn clockwise.
plt.hist(df["Weight"], bins=10)
plt.xlabel("Weight")
plt.ylabel("Frequency")

plt.subplot(3, 3, 8) # Specfies total rows, columns and image #
                     # where images are drawn clockwise.
plt.hist(df["Height"], bins=10)
plt.xlabel("Height")
plt.ylabel("Frequency")


plt.show()

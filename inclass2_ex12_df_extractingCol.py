import pandas as pd
path = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/bodyfat.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

df2 = df[["Height", "Waist","Weight","Pct.BF"]]
# Show DataFrame
print("\n*** DataFrame ***")
print (df2)

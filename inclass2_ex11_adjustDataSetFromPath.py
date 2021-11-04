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

print("\n FIRST 2 ROWS") # Prints title with space before.
print(df.head(2))

print("\n LAST 2 ROWS")
print(df.tail(2))

# Show data types for each columns.
print("\n DATA TYPES") # Prints title with space before.
print(df.dtypes)

# Show statistical summaries for numeric columns.
print("\nSTATISTIC SUMMARIES for NUMERIC COLUMNS")
print(df.describe().round(2))
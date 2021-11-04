import pandas as pd

# Import data into a DataFrame.
path = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/babysamp-98.txt"
df = pd.read_table(path, skiprows=1,
                   delim_whitespace=True,
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
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
print(df.describe())

# Show summaries for objects like dates and strings.
print("\nSTATISTIC SUMMARIES for DATE and STRING COLUMNS")
print(df.describe(include=['object']))

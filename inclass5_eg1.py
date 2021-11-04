import pandas as pd
DRIVER_PATH        = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_FILE ='grades.csv'
dataset     = { "NumericGrade":[99,98,84], "LetterGrade":['A+', 'A', 'B']}
dfOut       = pd.DataFrame( data = dataset)
print(dataset)

# Here I have decided to use a tab separator.
# The default separator is a comma which also could work.
dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep=',')

# Since I saved the file with a tab separator the instruction
# that reads the content must also use a tab separator.
dfIn        = pd.read_csv(DRIVER_PATH + CSV_FILE, sep=',')
print(dfIn.head(2))

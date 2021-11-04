import pandas as pd

# Define empty data frame structure.
df = pd.DataFrame(columns=['City', 'Temperature'])

# Add rows of data.
df = df.append({'City':'Mumbai', 'Temperature':23.0}, ignore_index=True)
df = df.append({'City':'Beijing', 'Temperature':-11.0}, ignore_index=True)

# Show original data frame.
print("Data frame with original data in Celsius:")
print(df)

# Show all columns of the data frame.
def getColumnPosition(df, columnName):
    columnList = list(df.keys())
    # Show all columns of the data frame in a list.
    print(columnList)
    columnPosition = 0
    for i in range(0, len(columnList)):
        if(columnList[i]==columnName):
            columnPosition = i
            break # Exit the loop.
    return columnPosition

# Update cell values - one at a time.
tempColumnPosition = getColumnPosition(df, "Temperature")
for i in range(0, len(df)):
    celsius = df.iloc[i]['Temperature']
    df.iat[i, tempColumnPosition] = celsius*9.0/5.0 + 32

print("\nDataframe after changed to Fahrenheit: ")
print(df)

tempColumnPosition = getColumnPosition(df, "City")
for i in range(0, len(df)):
    cityName = df.iloc[i]['City']
    df.iat[i, tempColumnPosition] = 'The city of '+cityName

print("\nDataframe after changed value of City: ")
print(df)
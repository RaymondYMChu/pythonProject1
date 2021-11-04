import pandas_datareader as pdr
import datetime
import pandas as pd

# Allow the full width of the data frame to show.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("------------------------------------------")
print("Stock Report Menu Options")
print("------------------------------------------")
print("1. Report changes for a stock\n2. Quit ")

options = int(input(""))
stockSymbol = input("enter the stock symbol\n")
numDay = int(input("enter the number of days\n"))

dt = datetime.date.today()
dtPast = dt + datetime.timedelta(days=-numDay)

print("***************************************************")
print("Daily Percent Changes - " + str(dtPast) + " to " + str(dt) + " * " + stockSymbol + " *")
print("***************************************************")


def getStock(stk):
    # Set and show dates.
    # Call Yahoo finance to get stock data for the stock provided.
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))
    # Return a dataframe containing stock data to the calling instruction.
    return df


dfApple = getStock(stockSymbol)
print(dfApple)
numRows = len(dfApple)
# Show the latest 'Close' price.
print("\nShowing the most recent closing price.")
print(dfApple.iloc[numRows - 1]['Close'])  # Referencing rows then columns
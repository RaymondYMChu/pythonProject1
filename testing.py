import pandas_datareader as pdr
import datetime
import pandas as pd

# Allow the full width of the data frame to show.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("------------------------------------------")
print("Stock Report Menu Options")
print("------------------------------------------")
stockSymbol = input("enter the stock symbol\n")
numDay = int(input("enter the number of days\n"))
dt = datetime.date.today()
dtPast = dt + datetime.timedelta(days=-numDay)
print("***************************************************")
print("Daily Percent Changes - "+str(dtPast)+" to "+str(dt)+" * "+stockSymbol.upper()+" *")
print("***************************************************")
def getStock(stk):
   # Set and show dates.
   # Call Yahoo finance to get stock data for the stock provided.
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))
   # Return a dataframe containing stock data to the calling instruction.
    return df
df1 = getStock(stockSymbol)
df2 = df1[['Close','Volume']]
df2['Price'] =0
print(df2)


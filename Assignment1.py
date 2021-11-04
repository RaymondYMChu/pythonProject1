import pandas_datareader as pdr
import datetime
import pandas as pd

# Allow the full width of the data frame to show.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Put a While loop to make sure Stock Report Menu Options will repeat to show up as long as user choose option 1
while True:
    print("------------------------------------------")
    print("Stock Report Menu Options")
    print("------------------------------------------")
    options = int(input("1. Report changes for a stock\n2. Quit\n"))

# Put a If function to ask for Stock Symbol and Number of days only if user choose option 1
    if options==1:
        stockSymbol = input("enter the stock symbol\n")
        numDay = int(input("enter the number of days\n"))
        dt = datetime.date.today()
        dtPast = dt + datetime.timedelta(days=-numDay)

# Set and show dates.
        print("*************************************************************")
        print("Daily Percent Changes - "+str(dtPast)+" to "+str(dt)+" * "+stockSymbol.upper()+" *")
        print("*************************************************************")
        def getStock(stk):

# Call Yahoo finance to get stock data for the stock provided.
            df = pdr.get_data_yahoo(stk,
                                    start=datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
                                    end=datetime.datetime(dt.year, dt.month, dt.day))

# Return a dataframe containing stock data to the calling instruction.
            return df

# create a new data frame to trigger the def getStock
        df1 = getStock(stockSymbol)

# create a another data frame to only extract Close and Volume
        df2 = df1[['Close','Volume']]

#command below is used to avoid warning of using copy of dataframe is on
        pd.options.mode.chained_assignment = None
        df2['Volume % Change'] = 0.0
        df2['Close % Change'] = 0.0
        volChange_idx = 2
        closeChange_idx = 3

#for loop to calculate the volume change and close price change percentage
        for i in range(0,len(df2)-1):
            closeChange = round(((df2.iloc[i+1]['Close']-df2.iloc[i]['Close'])/df2.iloc[i]['Close']),4)
            volChange = round(((df2.iloc[i+1]['Volume']-df2.iloc[i]['Volume'])/df2.iloc[i]['Volume']),4)
            df2.iat[i+1,volChange_idx] = volChange
            df2.iat[i+1,closeChange_idx]= closeChange
        print(df2)
        print("------------------------------------------")
        print("Summary of Cumulative Changes for "+stockSymbol)
        print("------------------------------------------")
        print(str(dtPast) + " to " + str(dt))

# to calculate the cumulative volume and close change from first past day to latest
        cumVolChange = round(((df2.iloc[len(df2)-1]['Volume']-df2.iloc[0]['Volume'])/df2.iloc[0]['Volume']),3)
        cumCloseChange = round(((df2.iloc[len(df2) - 1]['Close'] - df2.iloc[0]['Close']) / df2.iloc[0]['Close']),3)
        print("% Volume Change:       "+str(cumVolChange))
        print("% Close Price Change:  "+str(cumCloseChange))
        continue

# program will end if user to option 2
    if options==2:
        break


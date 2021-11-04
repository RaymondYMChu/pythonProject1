def showBalanceSchedule(firstName, balance, interestRate, yearsRemaining):
    yearCount=1;
    print("*BALANCE FORECAST for "+firstName+" *")
    if interestRate==0:
        print("NA")
    else:
        counter = 0;
        for counter in range(0,yearsRemaining):
            balance=balance*interestRate
            roundedBalance = round(balance, 2)
            print("Year " + str(yearCount) + ": " + str(roundedBalance))
            yearCount=yearCount+1
    print("")
showBalanceSchedule("Louise", 5.25, 1.07, 7)
showBalanceSchedule("Larry", 52.25, 0, 6)
showBalanceSchedule("Mehri", 152.25, 1.15, 6)

class BankAccount:  # Declare class.
    accountNumber = 0
    balance = 0
    firstName = ""
    lastName =""

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, accountNumber, balance, firstName, lastName):
        self.accountNumber = accountNumber
        self.balance = balance
        self.firstName = firstName
        self.lastName = lastName

    # Declare a function to display details about the child.
    def showDetail(self):
        print("The customer name is:   " + self.firstName+" "+self.lastName);
        print("Account Number " + str(self.accountNumber) + " balance: " + str(self.balance*1.03));

customerA = BankAccount(123, 500, "Raymond", "Chu")
customerA.showDetail()
customerB = BankAccount(456, 1000, "Peggy", "Chu")
customerB.showDetail()
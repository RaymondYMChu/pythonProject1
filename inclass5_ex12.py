class Child:  # Declare class.
    age = 0  # Declare and initialize age property.
    firstName = ""  # Declare and initialize firstName property.
    lastName = "" # Declare and initialize lastName Property

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self,firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    # Declare a function to display details about the child.
    def showDetail(self):
        print("The child's name is:   " + self.firstName + " "+self.lastName);
        print(self.firstName + "'s age is: " + str(self.age));

childA = Child("Jenny","Chan", 5)
childA.showDetail()
childB = Child("Raymond","Chu",20)
childB.showDetail()
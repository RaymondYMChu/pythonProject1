# This function receives a first middle and last name as parameters and displays
# it as formatted output.
def showFullName(firstName, middleName, lastName):
    # Python requires that all code belonging to the function be indented.
    output = "* Full Name: " + firstName + " " + middleName + " " + lastName + " *"
    print(output);

# These instructions call our functions.
showFullName("Raymond", "Yui Man", "Chu")


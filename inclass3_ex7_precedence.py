def displayContent(x):
    
    print('Inside the function the variable \'a\'=' + str(a))
    print('The parameter x=' + str(x))
    return # Locally declared variables die here when the function exits.

a = 100
displayContent(a)
print("The global value for \'a\'=" + str(a))

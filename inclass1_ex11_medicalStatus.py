def showMedicalStatus(firstName, age, highBloodPressure):
    if (age>=55 and highBloodPressure == True):
        print("Medical alert: "+firstName+" see a doctor.")
    elif (age< 55 and highBloodPressure == True):
        print("Warning: "+firstName+", seeing a doctor is recommended.")
    else:
        print(firstName+", you are in good health. See you next checkup.")

# Code for this function goes here.

showMedicalStatus("Bob", 60, True)
showMedicalStatus("Jane", 60, False)
showMedicalStatus("Brad", 28, True)

def showLetterGrade(percentage):
    if percentage >=90:
        print("The grade " + str(percentage) + " is A.")
    elif percentage >=70:
        print("The grade " + str(percentage) + " is C.")
    elif percentage >=50:
        print("The grade " + str(percentage) + " is F.")
    # if-elif-else series goes here inside the function.
showLetterGrade(95)
showLetterGrade(72)
showLetterGrade(51)

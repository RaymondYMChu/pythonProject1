def showReadingGlassesOrder(firstName,lastName,address,country,lenses,blueLight):
    print("***************************************")
    print(firstName+" "+lastName)
    print(address+", "+country)
    print("_______________________________________")
    if blueLight == True:
        print ("Lenses: "+str(lenses)+"x   (Blue light protection included)")
    else:
        print("Lenses: " + str(lenses) + "x")
    if country == "Canada":
        print("Shipping charges are $25.00.")
    elif country == "US":
        print("Shipping charges are $15.00.")
    elif country == "Mexico":
        print("Shipping charges are $26.50.")
    print("")

showReadingGlassesOrder("Akshay", "Tandon","12 Peaceful Place", "Canada", 1.25, False)
showReadingGlassesOrder("Merella", "Fernandez","126 Main Street", "Canada", 1.35, True)
showReadingGlassesOrder("Rachel", "Nichols","18 Sunset Blvd", "US", 1.05, True)
showReadingGlassesOrder("Maria", "Dulce","Paseo de la Reforma", "Mexico", 1.30, False)
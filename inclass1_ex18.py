def showFruitList(fruitList):
    print("\n*** DISPLAYING ARRAY CONTENTS");

    # Loop from 0 to 1 - length of array.
    for i in range(len(fruitList)):
        print(fruitList[i])

# Create array.
fruit = ["apples"]

# Add items to array.
fruit.append("pears")
fruit.insert(0, "plums")

# Remove third element (counting starts at 0).
fruit.pop(2)
# add items requested from Ex19
fruit.append("bananas")
fruit.append("dates")
fruit.append("peaches")
# Show array contents.
showFruitList(fruit)


numbers = [1.3,2.6,8.9,11.5,14.8]
print("The array length is " + str(len(numbers))  + ".")
for index in range(0, len(numbers)):
    print("index " + str(index) + ": " + str(numbers[index]))

print("\nHere is the list again.\n")

for number in numbers:
    print(number)

# Searches for match in an array of characters and starts count at 0.
sentence = "A lazy dog jumped over a log"
print("Starting position: " + str(sentence.find('dog')))

# When item not found, -1 is returned.
sentence = "A lazy dog jumped over a log"
print("Starting position: " + str(sentence.find('cat')))

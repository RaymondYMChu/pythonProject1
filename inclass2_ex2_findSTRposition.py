text = "She sells seashells by the sea shore."
positions = []
for i in range(0, len(text) - 2):
    if (text[i:i + 3] == "sea"):
        positions.append(i)
print(positions)

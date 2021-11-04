import matplotlib.pyplot as plt

# Plot scatter of x and y coordinates.
poundsA  = [120, 110, 160]
inchesA  = [50, 48, 68]
poundsB  = [121, 108, 150, 121, 121, 146]
inchesB  = [49, 45, 85, 46, 50, 85]


plt.scatter(poundsA, inchesA, color='orange', label='Student Region A')
plt.scatter(poundsB, inchesB, color='green', label='Student Region B')

# Add a legend, axis labels, and title.
plt.legend()
plt.xlabel("Height(Inches)")
plt.ylabel("Weight(Pounds)")
plt.title('Height vs. Weight for Students Region A and B')

plt.show()
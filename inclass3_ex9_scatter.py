import matplotlib.pyplot as plt

# Plot scatter of x and y coordinates.
pounds  = [120, 110, 160]
inches  = [50, 48, 68]

plt.scatter(pounds, inches, color='orange', label='Student Region A')

# Add a legend, axis labels, and title.
plt.legend()
plt.xlabel("Height(Inches)")
plt.ylabel("Weight(pounds)")
plt.title('Height vs. Weight for Students Region A')

plt.show()

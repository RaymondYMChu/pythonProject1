import matplotlib.pyplot as plt
import numpy as np

NUM_MEANS     = 4
NUM_GROUPS    = 3
bc_means      = [20, 35, 30, 35]
alberta_means = [25, 32, 34, 20]
saskatchewan_means = [18, 28, 32, 24]

# This generates indices from 0 to 3 in a format that is accepted for
# plotting bar charts.
ind = np.arange(NUM_MEANS)
print(ind)
width = 0.25
plt.bar(ind-width, bc_means, width, label='BC')
plt.bar(ind, alberta_means, width, label='AB')
plt.bar(ind + width, saskatchewan_means, width, label='SA')

plt.ylabel('Revenue')
plt.title('Quarterly Revenue by Province')

plt.xticks(ind + width / NUM_GROUPS, ('Q1', 'Q2', 'Q3', 'Q4'))
plt.legend(loc='best')
plt.show()


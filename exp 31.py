import numpy as np
import matplotlib.pyplot as plt

# Sample data
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)

# X-axis positions
index = np.arange(len(men_means))
bar_width = 0.5

# Plot stacked bars
plt.bar(index, men_means, bar_width,
        yerr=men_std, label='Men')

plt.bar(index, women_means, bar_width,
        bottom=men_means, yerr=women_std, label='Women')

# Labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(index, ['G1', 'G2', 'G3', 'G4', 'G5'])
plt.legend()

# Display plot
plt.show()

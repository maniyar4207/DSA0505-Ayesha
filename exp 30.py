import numpy as np
import matplotlib.pyplot as plt

# Sample data
men_scores = (22, 30, 35, 35, 26)
women_scores = (25, 32, 30, 35, 29)

# Number of groups
groups = len(men_scores)

# X-axis positions
index = np.arange(groups)
bar_width = 0.35

# Create bar plot
plt.bar(index, men_scores, bar_width, label='Men')
plt.bar(index + bar_width, women_scores, bar_width, label='Women')

# Labels and title
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")
plt.xticks(index + bar_width / 2, ['G1', 'G2', 'G3', 'G4', 'G5'])
plt.legend()

# Display plot
plt.show()

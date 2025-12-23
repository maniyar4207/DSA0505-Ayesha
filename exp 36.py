import matplotlib.pyplot as plt

# Sample data for three groups
group1_height = [150, 160, 165, 170, 175]
group1_weight = [50, 55, 60, 65, 70]

group2_height = [155, 165, 170, 175, 180]
group2_weight = [52, 58, 63, 68, 73]

group3_height = [160, 170, 175, 180, 185]
group3_weight = [55, 60, 65, 70, 75]

# Create scatter plot
plt.scatter(group1_height, group1_weight, color='red', label='Group 1', marker='o')
plt.scatter(group2_height, group2_weight, color='blue', label='Group 2', marker='s')
plt.scatter(group3_height, group3_weight, color='green', label='Group 3', marker='^')

# Add labels and title
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Scatter Plot of Height vs Weight for Three Groups')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

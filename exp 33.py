import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot with empty circles
plt.scatter(x, y, facecolors='none', edgecolors='blue')

# Labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot with Empty Circles")

# Display plot
plt.show()

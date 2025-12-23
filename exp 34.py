import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Generate random sizes for balls
sizes = np.random.rand(50) * 1000

# Create scatter plot
plt.scatter(x, y, s=sizes, alpha=0.6)

# Labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot with Different Ball Sizes")

# Display plot
plt.show()

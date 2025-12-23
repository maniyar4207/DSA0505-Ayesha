import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot
plt.scatter(x, y)

# Labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot of Random Distribution")

# Display plot
plt.show()

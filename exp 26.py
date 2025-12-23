import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 6, 7, 8, 9]
y4 = [10, 8, 6, 4, 2]

# Create multiple plots (2 rows, 2 columns)

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title("Plot 4")

# Adjust layout
plt.tight_layout()

# Show all plots
plt.show()

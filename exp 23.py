import matplotlib.pyplot as plt

x = []
y = []

# Read data from text file
with open("test.txt", "r") as file:
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

# Plot the line graph
plt.plot(x, y)

# Labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Graph from Text File")

# Show the graph
plt.show()

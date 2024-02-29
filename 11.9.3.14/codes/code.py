import numpy as np
import matplotlib.pyplot as plt

# Load data from data.dat file
data = np.loadtxt('data.dat')

# Extract n and y(n) values
n_values = data[:, 0]
y_values = data[:, 1]

# Plot y(n)
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')

# Set labels and title
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.title('Plot of $y(n)$')
plt.grid(True)

# Show plot
plt.savefig('plot.png')
plt.show()


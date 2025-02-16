import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Define the function to integrate
def f(x):
    # This function will return the square of x
    return x ** 2

# Integration limits
a = 0  # Lower limit
b = 2  # Upper limit

# Generate x values for plotting
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Create a plot
fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, 'r', linewidth=2)

# Fill area under curve between a and b
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Configure plot limits and labels
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Draw vertical lines at integration limits
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph of Integration f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Number of random samples for Monte Carlo
N = 100000

# Generate random points in [a, b]
x_random = np.random.uniform(a, b, N)

# Calculate f(x) for random points
f_values = f(x_random)

# Monte Carlo estimate of the integral
mc_integral = (b - a) * np.mean(f_values)

# Analytical integration using quad
quad_result, quad_error = spi.quad(f, a, b)

# Print results for comparison
print("Monte Carlo approximation:", mc_integral)
print("Quad result:", quad_result, "with error:", quad_error)
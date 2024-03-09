import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    _, _, mandelbrot_set_data = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandelbrot_set_data.T, extent=(xmin, xmax, ymin, ymax))
    plt.show()

# Define the region of the complex plane to plot
xmin, xmax, ymin, ymax = -2.0, 2.0, -2.0, 2.0

# Set the width and height of the plot (more pixels = higher resolution)
width, height = 500, 500

# Maximum number of iterations for the Mandelbrot calculation
max_iter = 100

# Plot the Mandelbrot set
plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

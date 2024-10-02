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
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=1000, height=1000, max_iter=256):
    x, y = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height))
    mandelbrot_set_data = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_set_data.T, extent=(xmin, xmax, ymin, ymax), cmap='hot', origin='lower')
    plt.title('Mandelbrot Set')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.show()

# Define the region of the complex plane to plot (adjust these parameters for different views)
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
plot_mandelbrot(xmin, xmax, ymin, ymax)

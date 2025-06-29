import numpy as np

# Monte Carlo method to estimate the area of the Mandelbrot set
def mandelbrot_check(c_real, c_imag, max_iter=10000):
    """Check if a complex number belongs to the Mandelbrot set."""
    z_real, z_imag = 0, 0
    for _ in range(max_iter):
        z_real, z_imag = z_real**2 - z_imag**2 + c_real, 2 * z_real * z_imag + c_imag
        if z_real**2 + z_imag**2 > 4:
            return False
    return True

# Define bounding box
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
box_area = (x_max - x_min) * (y_max - y_min)

# Monte Carlo integration
total_points = 0
inside_points = 0
batch_size = 2000
total_samples = 10000000

# Process batches
for _ in range(0, total_samples, batch_size):
    rand_x = np.random.uniform(x_min, x_max, batch_size)
    rand_y = np.random.uniform(y_min, y_max, batch_size)
    inside = np.array([mandelbrot_check(x, y) for x, y in zip(rand_x, rand_y)])
    inside_points += np.sum(inside)
    total_points += batch_size

    # Estimate Mandelbrot set area
    estimated_area = (inside_points / total_points) * box_area
    print(f"Estimated Mandelbrot Set Area\t {estimated_area} \t {total_points}")
 

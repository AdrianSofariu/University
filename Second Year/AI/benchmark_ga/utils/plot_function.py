import numpy as np
import matplotlib.pyplot as plt


def plot_function(func):
    """
    Plot the function in 2D and 3D.
    :param func: BenchmarkFunction instance
    :return: None
    """
    x_bounds, y_bounds = func.bounds()
    x = np.linspace(*x_bounds, 100)
    y = np.linspace(*y_bounds, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.vectorize(lambda x, y: func.evaluate(x, y))(X, Y)

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    cp = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(cp)
    plt.title(f"Contour Plot: {func.name()}")
    plt.xlabel("x")
    plt.ylabel("y")

    ax = plt.subplot(1, 2, 2, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(f"Surface Plot: {func.name()}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")

    plt.tight_layout()
    plt.show()

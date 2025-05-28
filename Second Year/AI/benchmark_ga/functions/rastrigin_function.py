import numpy as np
from .base_function import BenchmarkFunction


class RastriginFunction(BenchmarkFunction):
    """
    Standard Rastrigin benchmark function for optimization.
    """

    def evaluate(self, x, y):
        """
        Compute the Rastrigin function value at (x, y).
        f(x, y) = 20 + x^2 + y^2 - 10 * (cos(2πx) + cos(2πy))
        """
        return 20 + x**2 + y**2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))

    def bounds(self):
        """
        Return domain bounds for x and y.
        """
        return (-5.12, 5.12), (-5.12, 5.12)

    def name(self):
        return "Rastrigin"

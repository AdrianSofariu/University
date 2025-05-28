import numpy as np
from .base_function import BenchmarkFunction


class AckleyFunction(BenchmarkFunction):
    """
    Standard Ackley benchmark function for optimization.
    """

    def evaluate(self, x, y):
        """
        Compute the Ackley function value at (x, y).
        f(x, y) = -20 * exp(-0.2 * sqrt(0.5 * (x² + y²)))
                  - exp(0.5 * (cos(2πx) + cos(2πy))) + e + 20
        """
        part1 = -0.2 * np.sqrt(0.5 * (x**2 + y**2))
        part2 = 0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))
        return -20 * np.exp(part1) - np.exp(part2) + 20 + np.e

    def bounds(self):
        """
        Return domain bounds for x and y.
        """
        return (-32, 32), (-32, 32)

    def name(self):
        return "Ackley"

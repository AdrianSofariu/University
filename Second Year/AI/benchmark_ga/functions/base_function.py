from abc import ABC, abstractmethod


class BenchmarkFunction(ABC):
    """
    This module defines an abstract base class for benchmark functions.
    It provides a template for creating specific benchmark functions
    by enforcing the implementation of three methods:
    - evaluate: to compute the function value given x and y coordinates.
    - bounds: to define the input bounds for the function.
    - name: to return the name of the function.
    The purpose of this module is to provide a consistent interface
    for different benchmark functions, making it easier to implement
    """

    @abstractmethod
    def evaluate(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def bounds(self) -> tuple:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

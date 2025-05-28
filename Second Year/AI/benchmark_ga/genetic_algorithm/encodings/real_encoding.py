import numpy as np


class RealEncoding:
    """
    Handles real-valued encoding initialization and crossover operations.
    This class is responsible for creating a population of real-valued individuals,
    performing crossover between pairs of individuals, and ensuring that the offspring
    remain within specified bounds.
    """
    def __init__(self, config, x_bounds, y_bounds):
        self.size = config["population_size"]
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.crossover_method = config["crossover_method"]
        self.blx_alpha = config.get("blx_alpha", 0.5)

        self.crossover_map = {
            "arithmetic": self.arithmetic_crossover,
            "blx": self.blx_alpha_crossover,
        }
        if self.crossover_method not in self.crossover_map:
            raise ValueError(f"Unknown crossover method: {self.crossover_method}")

    def initialize_population(self):
        """
        Initializes a population of individuals using real-valued encoding.

        Returns:
            np.ndarray: A population array of shape (population_size, 2) with real-valued individuals.
        """
        return np.random.uniform(
            [self.x_bounds[0], self.y_bounds[0]],
            [self.x_bounds[1], self.y_bounds[1]],
            (self.size, 2)
        )

    def mutate(self, individual, mutation_rate):
        """
        Perform mutation on a real-valued individual with a given mutation rate.
        :param individual: real-valued individual to mutate
        :param mutation_rate: probability of mutation for each gene
        :return: mutated individual
        """
        mutant = individual.copy()
        if np.random.rand() < mutation_rate:
            mutant[0] += np.random.normal(0, 0.1)
            mutant[0] = np.clip(mutant[0], *self.x_bounds)
        if np.random.rand() < mutation_rate:
            mutant[1] += np.random.normal(0, 0.1)
            mutant[1] = np.clip(mutant[1], *self.y_bounds)
        return mutant

    def arithmetic_crossover(self, p1, p2):
        """
        Perform arithmetic crossover between two real-valued parents.
        :param p1: first parent
        :param p2: second parent
        :return: two offspring
        """
        alpha = np.random.rand()
        c1 = alpha * p1 + (1 - alpha) * p2
        c2 = alpha * p2 + (1 - alpha) * p1
        return c1, c2

    def blx_alpha_crossover(self, p1, p2):
        """
        Perform BLX-α crossover between two real-valued parents.
        :param p1: first parent
        :param p2: second parent
        :return: two offspring
        """
        diff = np.abs(p1 - p2)
        low = np.minimum(p1, p2) - self.blx_alpha * diff
        high = np.maximum(p1, p2) + self.blx_alpha * diff
        c1 = np.random.uniform(low, high)
        c2 = np.random.uniform(low, high)
        return c1, c2

    def crossover(self, p1, p2, crossover_rate):
        if np.random.rand() > crossover_rate:
            return p1.copy(), p2.copy()
        return self.crossover_map[self.crossover_method](p1, p2)

    def decode_population(self, population):
        """
        Decode real-valued population to tuples of (x, y) pairs.
        :param population: array of real-valued individuals
        :return: list of tuples representing decoded individuals
        """
        return [tuple(ind) for ind in population]

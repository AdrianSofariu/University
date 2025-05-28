import numpy as np


class BinaryEncoding:
    """
    Handles binary encoding initialization and crossover operations.
    This class is responsible for creating a population of binary strings,
    performing crossover between pairs of individuals, and decoding the
    binary strings into real-valued numbers within specified bounds.
    """
    def __init__(self, config, x_bounds, y_bounds):
        self.size = config["population_size"]
        self.length = config["binary_length"]
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.crossover_method = config["crossover_method"]

        # Map crossover names to instance methods
        self.crossover_map = {
            "1point": self.one_point_crossover,
            "2point": self.two_point_crossover,
        }
        if self.crossover_method not in self.crossover_map:
            raise ValueError(f"Unknown crossover method: {self.crossover_method}")

    def initialize_population(self):
        """
        Initializes a population of individuals using binary encoding.

        Returns:
            np.ndarray: A population array of shape (population_size, total_bit_length)
                        where each individual is a binary string.
        """
        return np.random.randint(0, 2, (self.size, self.length * 2))

    def mutate(self, individual, mutation_rate):
        """
        Perform mutation on a binary string with a given mutation rate.
        :param individual: binary string to mutate
        :param mutation_rate: probability of mutation for each bit
        :return:
        """
        mutant = individual.copy()
        for i in range(len(mutant)):
            if np.random.rand() < mutation_rate:
                mutant[i] ^= 1  # bit flip
        return mutant

    def one_point_crossover(self, p1, p2):
        """
        Perform one-point crossover between two binary strings.
        :param p1: first parent binary string
        :param p2: second parent binary string
        :return: two offspring binary strings
        """
        point = np.random.randint(1, len(p1))
        c1 = np.concatenate([p1[:point], p2[point:]])
        c2 = np.concatenate([p2[:point], p1[point:]])
        return c1, c2

    def two_point_crossover(self, p1, p2):
        """
        Perform two-point crossover between two binary strings.
        :param p1: first parent binary string
        :param p2: second parent binary string
        :return: two offspring binary strings
        """
        points = sorted(np.random.choice(range(1, len(p1)), 2, replace=False))
        c1 = np.concatenate([p1[:points[0]], p2[points[0]:points[1]], p1[points[1]:]])
        c2 = np.concatenate([p2[:points[0]], p1[points[0]:points[1]], p2[points[1]:]])
        return c1, c2

    def crossover(self, p1, p2, crossover_rate):
        """
        Perform crossover between two binary strings based on the crossover rate.
        :param p1: first parent binary string
        :param p2: second parent binary string
        :param crossover_rate: probability of performing crossover
        :return: two offspring binary strings
        """
        if np.random.rand() > crossover_rate:
            return p1.copy(), p2.copy()
        return self.crossover_map[self.crossover_method](p1, p2)

    def decode_population(self, population):
        """
        Decode binary-encoded population to real-valued (x, y) pairs.
        :param population: ndarray of binary individuals
        :return: list of tuples [(x1, y1), ..., (xn, yn)]
        """

        def decode(bits, bounds):
            integer = int("".join(str(b) for b in bits), 2)
            max_val = 2 ** len(bits) - 1
            return bounds[0] + (bounds[1] - bounds[0]) * integer / max_val

        decoded = []
        for individual in population:
            x_bits = individual[:self.length]
            y_bits = individual[self.length:]
            x = decode(x_bits, self.x_bounds)
            y = decode(y_bits, self.y_bounds)
            decoded.append((x, y))
        return decoded

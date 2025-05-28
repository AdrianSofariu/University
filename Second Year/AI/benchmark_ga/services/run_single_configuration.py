import numpy as np
from genetic_algorithm.ga_core import GA_Core


def run_single_ga_experiment(config, benchmark_function):
    """
    Run a single experiment of the Genetic Algorithm with the given configuration and benchmark function.
    :param config: configuration dictionary containing GA parameters
    :param benchmark_function: the function to be optimized
    :return: a dictionary containing:
        - function_name: name of the benchmark function
        - encoding: encoding method used
        - crossover: crossover method used
        - best_solution: best solution found by the GA
        - best_fitness: fitness of the best solution
    """
    # Extract bounds
    x_bounds, y_bounds = benchmark_function.bounds()

    # Define fitness function
    def fitness(individual):
        x, y = individual
        return benchmark_function.evaluate(x, y)

    # Initialize and run GA
    ga = GA_Core(config, fitness, x_bounds, y_bounds)
    best_solution, best_fitness, _ = ga.evolve()

    return {
        "function_name": benchmark_function.name(),
        "encoding": config["encoding"],
        "crossover": config["crossover_method"],
        "best_solution": tuple(best_solution),
        "best_fitness": float(best_fitness)
    }

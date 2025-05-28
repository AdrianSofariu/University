import numpy as np
from .encodings.factory import get_encoding_handler  # Adjust import as per your project structure


class GA_Core:
    """
    Genetic Algorithm core engine supporting modular encodings.

    Attributes:
        encoding: Encoding class instance (binary or real-valued).
        fitness_func: Function to evaluate individuals (expects real-valued decoded individuals).
        config: Dictionary containing GA parameters:
            - population_size
            - mutation_rate
            - crossover_rate
            - generations
            - tournament_size
    """

    def __init__(self, config, fitness_func, x_bounds, y_bounds):
        self.config = config
        self.fitness_func = fitness_func
        self.population_size = config.get("population_size", 100)
        self.mutation_rate = config.get("mutation_rate", 0.05)
        self.crossover_rate = config.get("crossover_rate", 0.8)
        self.generations = config.get("generations", 100)
        self.tournament_size = config.get("tournament_size", 3)

        # Create encoding instance via factory function
        self.encoding = get_encoding_handler(config, x_bounds, y_bounds)

        # Initialize population
        self.population = self.encoding.initialize_population()
        self.best_solution = None
        self.best_fitness = np.inf
        self.history = []  # best fitness per generation

    def tournament_selection(self, fitnesses):
        selected_indices = np.random.choice(len(self.population), self.tournament_size, replace=False)
        tournament_fitnesses = [fitnesses[i] for i in selected_indices]
        winner_idx = selected_indices[np.argmin(tournament_fitnesses)]  # minimize fitness
        return self.population[winner_idx]

    def evolve(self):
        for gen in range(self.generations):
            decoded_pop = self.encoding.decode_population(self.population)
            fitnesses = np.array([self.fitness_func(ind) for ind in decoded_pop])

            min_idx = np.argmin(fitnesses)
            if fitnesses[min_idx] < self.best_fitness:
                self.best_fitness = fitnesses[min_idx]
                self.best_solution = decoded_pop[min_idx]
            self.history.append(self.best_fitness)

            new_population = []
            while len(new_population) < self.population_size:
                p1 = self.tournament_selection(fitnesses)
                p2 = self.tournament_selection(fitnesses)

                c1_enc, c2_enc = self.encoding.crossover(p1, p2, self.crossover_rate)
                c1_mut = self.encoding.mutate(c1_enc, self.mutation_rate)
                c2_mut = self.encoding.mutate(c2_enc, self.mutation_rate)

                new_population.extend([c1_mut, c2_mut])

            self.population = np.array(new_population[:self.population_size])

        return self.best_solution, self.best_fitness, self.history

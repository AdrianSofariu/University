import numpy as np


def tournament_selection(population, fitnesses, k=3):
    """
       Tournament selection: Selects the best individual from k randomly chosen.

       Args:
           population: Current population.
           fitnesses: Fitness values for each individual.
           k: Number of individuals per tournament.

       Returns:
           Array of selected individuals.
    """
    selected = []
    for _ in range(len(population)):
        indices = np.random.choice(len(population), k)
        best_idx = indices[np.argmin(fitnesses[indices])]
        selected.append(population[best_idx])
    return np.array(selected)

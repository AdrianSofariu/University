# Configuration dictionary for GA parameters.
# Easily adjustable for experimenting with different settings.

CONFIG = {
    "population_size": 100,
    "generations": 150,
    "mutation_rate": 0.02,
    "crossover_rate": 0.8,
    "encoding": "binary",  # "real" or "binary"
    "crossover_method": "1point",  # "arithmetic", "blx", "1point", "2point"
    "blx_alpha": 0.8,
    "binary_length": 32,
    "seeds": [93, 68, 16, 42, 87,
              80, 72, 92, 31, 21,
              17, 7, 10, 59, 86,
              99, 35, 79, 44, 6,
              1, 14, 98, 55, 54,
              4, 18, 76, 95, 66]
}

import numpy as np
import pandas as pd
from tqdm import tqdm
from services.run_single_configuration import run_single_ga_experiment
from functions.rastrigin_function import RastriginFunction
from functions.ackley_function import AckleyFunction


def run_all_configurations(config_template, num_runs=30):
    """
    Run all configurations for the Genetic Algorithm experiments.
    :param config_template:
        A dictionary containing the base configuration for the GA.
        This should include parameters like population size, mutation rate, etc.
        The encoding and crossover method will be overridden by the specific configurations.
        Example:
        {
            "population_size": 100,
            "generations": 150,
            "mutation_rate": 0.02,
            "crossover_rate": 0.8,
            "seed": 42,
            "blx_alpha": 0.7,
            "binary_length": 32,
        }
    :param num_runs:
        Number of runs for each configuration.
        Default is 30.
        Run each configuration with a different random seed to ensure diversity in results.

    :return:
        - df_results: DataFrame containing all results.
        - df_summary: DataFrame summarizing the performance of each configuration.
    """

    # Define 8 configurations
    configs = [
        {"encoding": "real", "crossover_method": "arithmetic"},
        {"encoding": "real", "crossover_method": "blx"},
        {"encoding": "binary", "crossover_method": "1point"},
        {"encoding": "binary", "crossover_method": "2point"},
    ]

    # Define benchmark functions
    benchmark_funcs = [
        RastriginFunction(),
        AckleyFunction(),
    ]

    results = []

    # Iterate over each benchmark function and configuration
    for benchmark_func in benchmark_funcs:
        total_runs = len(configs) * num_runs
        print(f"\nRunning {total_runs} experiments for function: {benchmark_func.name()}\n")

        for conf in configs:
            for run_id in tqdm(range(num_runs), desc=f"{conf['encoding']} + {conf['crossover_method']} ({benchmark_func.name()})"):
                # Merge base config with encoding-specific settings
                config = config_template.copy()
                config.update(conf)

                # Use the seeds from the list of 30 seeds in the config
                seed = config["seeds"][run_id % len(config["seeds"])]

                # Seed numpy random number generator
                np.random.seed(seed)

                result = run_single_ga_experiment(config, benchmark_func)
                result["run_id"] = run_id
                results.append(result)

    df_results = pd.DataFrame(results)

    # Summarize performance
    df_summary = df_results.groupby(["function_name", "encoding", "crossover"]).agg(
        best=("best_fitness", "min"),
        mean=("best_fitness", "mean"),
        std=("best_fitness", "std"),
        median=("best_fitness", "median"),
    ).reset_index()

    print("\nSummary of Results:")
    print(df_summary.to_string(index=False))

    return df_results, df_summary

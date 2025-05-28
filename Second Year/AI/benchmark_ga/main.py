import numpy as np
import config
from functions.ackley_function import AckleyFunction
from functions.rastrigin_function import RastriginFunction

from services.run_all_configurations import run_all_configurations
from services.statistical_analysis_service import analyze_non_normalized_results
from services.visualisation_service import generate_all_ga_visualizations
from utils.plot_function import plot_function


if __name__ == "__main__":

    # Plot the benchmark functions
    ackley_func = AckleyFunction()
    plot_function(ackley_func)

    rastrigin_func = RastriginFunction()
    plot_function(rastrigin_func)

    # Run all configurations and generate visualizations
    df_results, df_summary = run_all_configurations(config.CONFIG, num_runs=30)
    generate_all_ga_visualizations(df_results, df_summary)
    analyze_non_normalized_results(df_results)

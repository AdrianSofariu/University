import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_mean_fitness_bars(summary_df):
    """
    Plot mean fitness with standard deviation bars for each crossover method and encoding.
    :param summary_df: DataFrame containing summary statistics of the results, for example:
        - function_name: name of the benchmark function
        - encoding: encoding method used
        - crossover: crossover method used
        - best: best fitness value
        - mean: mean fitness value
        - std: standard deviation of fitness values
        - median: median fitness value
    :return: None (displays plots)
    """
    for func_name in summary_df['function_name'].unique():
        plt.figure(figsize=(12, 8))
        data = summary_df[summary_df['function_name'] == func_name]

        pivot_mean = data.pivot(index='crossover', columns='encoding', values='mean')
        pivot_std = data.pivot(index='crossover', columns='encoding', values='std')

        crossover_types = pivot_mean.index.tolist()
        encoding_types = pivot_mean.columns.tolist()
        x = np.arange(len(crossover_types))
        width = 0.35

        for i, encoding in enumerate(encoding_types):
            plt.bar(
                x + (i - len(encoding_types) / 2 + 0.5) * width,
                pivot_mean[encoding],
                yerr=pivot_std[encoding],
                capsize=5,
                width=width,
                label=encoding
            )

        plt.xticks(x, crossover_types)
        plt.title(f"{func_name}: Mean Fitness with Std Deviation")
        plt.xlabel("Crossover Method")
        plt.ylabel("Mean Best Fitness")
        plt.legend(title="Encoding")
        plt.tight_layout()
        plt.show()


def plot_fitness_kde(results_df):
    """
    Plot Kernel Density Estimation (KDE) of best fitness for each encoding and crossover method.
    :param results_df: DataFrame containing the results of the experiments, for example:
        - function_name: name of the benchmark function
        - encoding: encoding method used
        - crossover: crossover method used
        - best_solution: best solution found by the GA
        - best_fitness: fitness of the best solution
    :return: None (displays plots)
    """
    for func_name in results_df['function_name'].unique():
        plt.figure(figsize=(12, 8))
        data = results_df[results_df['function_name'] == func_name]

        for _, group_data in data.groupby(['encoding', 'crossover']):
            label = f"{group_data['encoding'].iloc[0]} + {group_data['crossover'].iloc[0]}"
            sns.kdeplot(group_data['best_fitness'], label=label, fill=True)

        plt.title(f"{func_name}: Fitness KDE Curves")
        plt.xlabel("Best Fitness")
        plt.ylabel("Density")
        plt.legend(title="Configuration")
        plt.tight_layout()
        plt.show()


def plot_violin_fitness_distributions(results_df):
    """
    Plot violin plots of best fitness distributions for each encoding and crossover method.
    :param results_df: DataFrame containing the results of the experiments, for example:
        - function_name: name of the benchmark function
        - encoding: encoding method used
        - crossover: crossover method used
        - best_solution: best solution found by the GA
        - best_fitness: fitness of the best solution
    :return: None (displays plots)
    """
    for func_name in results_df["function_name"].unique():
        data = results_df[results_df["function_name"] == func_name].copy()
        data["group"] = data["encoding"] + " + " + data["crossover"]

        plt.figure(figsize=(12, 6))
        sns.violinplot(x="group", y="best_fitness", data=data, inner="box", hue="encoding",
                       palette={'binary': 'blue', 'real': 'orange'}, fill=True)
        plt.xticks(rotation=45)
        plt.title(f"{func_name}: Best Fitness Violin Plot by Configuration")
        plt.xlabel("Configuration")
        plt.ylabel("Best Fitness")
        plt.tight_layout()
        plt.show()


def plot_violin_fitness_distributions_with_noise(results_df):
    """
    Plot violin plots of best fitness distributions for each encoding and crossover method.
    Adds a tiny amount of noise to extremely low-variance data to ensure rendering of collapsed violins.

    :param results_df: DataFrame containing the results of the experiments, for example:
        - function_name: name of the benchmark function
        - encoding: encoding method used
        - crossover: crossover method used
        - best_solution: best solution found by the GA
        - best_fitness: fitness of the best solution
    :return: None (displays plots)
    """
    # Define a slightly larger noise magnitude specifically for violin plots.
    # This value is needed to make extremely low-variance data render.
    noise_magnitude_violin = 1e-8

    for func_name in results_df["function_name"].unique():
        # Create a copy to avoid modifying the original DataFrame
        data = results_df[results_df["function_name"] == func_name].copy()
        data["group"] = data["encoding"] + " + " + data["crossover"]

        # --- Apply noise to problematic configurations for rendering purposes ---
        # Target Rastrigin's binary configurations as they are known to cause issues.
        if func_name == 'Rastrigin':
            binary_1point_mask = (data['encoding'] == 'binary') & (data['crossover'] == '1point')
            binary_2point_mask = (data['encoding'] == 'binary') & (data['crossover'] == '2point')

            # Add random noise to 'best_fitness' for these specific groups
            # Only add if the actual std is very low, to avoid unnecessary noise for already spread data.

            # Process binary + 1point
            if binary_1point_mask.any():
                current_1point_std = data.loc[binary_1point_mask, 'best_fitness'].std()
                print(f"Rastrigin binary + 1point original std: {current_1point_std}")
                if current_1point_std < 1e-7:  # Use a slightly larger threshold for checking
                    data.loc[binary_1point_mask, 'best_fitness'] += np.random.normal(
                        0, noise_magnitude_violin, size=binary_1point_mask.sum()
                    )
                    data.loc[binary_1point_mask, 'best_fitness'] = np.maximum(0, data.loc[
                        binary_1point_mask, 'best_fitness'])  # Ensure non-negative
                    print(
                        f"Rastrigin binary + 1point std AFTER NOISE: {data.loc[binary_1point_mask, 'best_fitness'].std()}")

            # Process binary + 2point (also add noise for consistent rendering, even if it rendered before)
            if binary_2point_mask.any():
                current_2point_std = data.loc[binary_2point_mask, 'best_fitness'].std()
                print(f"Rastrigin binary + 2point original std: {current_2point_std}")
                if current_2point_std < 1e-7:  # Use a slightly larger threshold for checking
                    data.loc[binary_2point_mask, 'best_fitness'] += np.random.normal(
                        0, noise_magnitude_violin, size=binary_2point_mask.sum()
                    )
                    data.loc[binary_2point_mask, 'best_fitness'] = np.maximum(0, data.loc[
                        binary_2point_mask, 'best_fitness'])  # Ensure non-negative
                    print(
                        f"Rastrigin binary + 2point std AFTER NOISE: {data.loc[binary_2point_mask, 'best_fitness'].std()}")
        # --- End of noise application ---

        plt.figure(figsize=(12, 6))
        sns.violinplot(x="group", y="best_fitness", data=data, inner="box", hue="encoding",
                       palette={'binary': 'blue', 'real': 'orange'},
                       fill=True)
        plt.xticks(rotation=45, ha='right')
        plt.title(f"{func_name}: Best Fitness Violin Plot by Configuration")
        plt.xlabel("Configuration")
        plt.ylabel("Best Fitness")
        plt.tight_layout()
        plt.show()


def plot_fitness_kde_with_noise(results_df):
    """
    Plot Kernel Density Estimation (KDE) of best fitness for each encoding and crossover method.
    Adds a tiny amount of noise to extremely low-variance data (like Ackley Real BLX)
    to ensure rendering of collapsed KDE curves (sharp spikes).

    :param results_df: DataFrame containing the results of the experiments, for example:
        - function_name: name of the benchmark function
        - encoding: encoding method used
        - crossover: crossover method used
        - best_solution: best solution found by the GA
        - best_fitness: fitness of the best solution
    :return: None (displays plots)
    """
    # Define a very small noise magnitude for plotting purposes.
    noise_magnitude = 1e-15

    for func_name in results_df['function_name'].unique():
        plt.figure(figsize=(12, 8))
        # Create a copy to avoid modifying the original DataFrame passed to the function
        data = results_df[results_df['function_name'] == func_name].copy()

        for (encoding, crossover), group_data in data.groupby(['encoding', 'crossover']):
            label = f"{encoding} + {crossover}"

            current_group_data = group_data['best_fitness'].copy()  # Work on a copy of the series

            # Check if the standard deviation is effectively zero for KDE rendering
            # A common heuristic is to check if std is below a very small epsilon
            # Or, more directly, target the known problematic configurations
            if func_name == 'Ackley' and encoding == 'real' and crossover == 'blx':
                # Check if the actual std is very close to zero before adding noise
                # This avoids adding noise unnecessarily to already spread data.
                if current_group_data.std() < 1e-10:  # A threshold for "effectively zero" std
                    current_group_data += np.random.normal(0, noise_magnitude, size=len(current_group_data))
                    # Ensure fitness remains non-negative after adding noise
                    current_group_data = np.maximum(0, current_group_data)

            # Plot the KDE with the potentially modified data
            sns.kdeplot(current_group_data, label=label, fill=True)

        plt.title(f"{func_name}: Fitness KDE Curves")
        plt.xlabel("Best Fitness")
        plt.ylabel("Density")
        plt.legend(title="Configuration")
        plt.tight_layout()
        plt.show()


def generate_all_ga_visualizations(results_df, summary_df):
    """Call all visualization functions."""
    plot_mean_fitness_bars(summary_df)
    plot_fitness_kde_with_noise(results_df)
    plot_violin_fitness_distributions_with_noise(results_df)
    print("All visualizations generated.")

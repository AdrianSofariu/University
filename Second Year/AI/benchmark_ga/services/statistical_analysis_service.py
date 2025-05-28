import pandas as pd
from scipy.stats import f_oneway, kruskal
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import scikit_posthocs as sp


def analyze_normalized_results(df_results):
    """
    Perform statistical analysis on the results of the Genetic Algorithm experiments.
    This includes ANOVA and post-hoc tests, as well as visualizations.
    :param df_results: DataFrame containing the results of the experiments.
    :return: summary: A dictionary summarizing the results of the analysis.
    """
    summary = {}

    for func_name in df_results["function_name"].unique():
        df_func = df_results[df_results["function_name"] == func_name]
        print(f"\n📊 Analyzing {func_name}...\n")

        # Create groups for ANOVA
        group_labels = df_func["encoding"] + " + " + df_func["crossover"]
        df_func = df_func.copy()
        df_func["group"] = group_labels
        grouped = df_func.groupby("group")["best_fitness"].apply(list)

        # Run ANOVA
        f_stat, p_value = f_oneway(*grouped.values)
        print(f"ANOVA F-statistic = {f_stat:.4f}, p-value = {p_value:.4e}")
        summary[func_name] = {"anova": {"f_stat": f_stat, "p_value": p_value}}

        # Tukey HSD post-hoc test
        if p_value < 0.05:
            tukey = pairwise_tukeyhsd(
                endog=df_func["best_fitness"],
                groups=df_func["group"],
                alpha=0.05
            )
            print("\nPost-hoc (Tukey HSD):")
            print(tukey.summary())
            summary[func_name]["tukey"] = tukey

    return summary

def analyze_non_normalized_results(df_results):
    """
    Perform statistical analysis on the results of the Genetic Algorithm experiments.
    This includes Kruskal-Wallis H-test and Dunn's post-hoc tests, as well as visualizations.
    :param df_results: DataFrame containing the results of the experiments.
    :return: summary: A dictionary summarizing the results of the analysis.
    """
    summary = {}

    # --- Adjust pandas display options to show full DataFrame ---
    # Set max columns to None to display all columns
    pd.set_option('display.max_columns', None)
    # Set display width to a large number to prevent horizontal truncation
    pd.set_option('display.width', 1000)
    # Set max rows to None if you expect many rows and want to see all
    pd.set_option('display.max_rows', None)

    for func_name in df_results["function_name"].unique():
        df_func = df_results[df_results["function_name"] == func_name]
        print(f"\n📊 Analyzing {func_name} (Non-parametric tests)...\n")

        # Create groups for Kruskal-Wallis
        group_labels = df_func["encoding"] + " + " + df_func["crossover"]
        df_func = df_func.copy() # Ensure we're working on a copy to avoid SettingWithCopyWarning
        df_func["group"] = group_labels
        grouped_data = df_func.groupby("group")["best_fitness"].apply(list)

        # Run Kruskal-Wallis H-test
        # kruskal returns a tuple of (statistic, pvalue)
        h_stat, p_value = kruskal(*grouped_data.values)
        print(f"Kruskal-Wallis H-statistic = {h_stat:.4f}, p-value = {p_value:.4e}")
        summary[func_name] = {"kruskal": {"h_stat": h_stat, "p_value": p_value}}

        # Dunn's post-hoc test
        if p_value < 0.05: # Only perform post-hoc if overall test is significant
            # scikit_posthocs.posthoc_dunn requires a flat array of data and a corresponding array of group labels
            dunn_results = sp.posthoc_dunn(
                a=df_func,  # DataFrame containing the results
                val_col='best_fitness',  # Specify the column containing the values
                group_col='group',  # Corrected argument name to 'group_col'
                p_adjust='bonferroni'  # Common p-value adjustment method
            )
            print("\nPost-hoc (Dunn's Test with Bonferroni correction):")
            print(dunn_results) # Dunn's test returns a DataFrame
            summary[func_name]["dunn"] = dunn_results
        else:
            print("\nKruskal-Wallis H-test not significant, no post-hoc test performed.")

    # Reset pandas display options to default
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.max_rows')
    return summary

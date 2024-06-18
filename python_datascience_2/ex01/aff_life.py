import sys
import matplotlib.pyplot as plt

from load_csv import load


def aff_life(data, country):
    """
    Plots the life expectancy projections for a given country based on the
    provided dataset.

    Parameters:
    data (pandas.DataFrame): The dataset containing life expectancy projections
    for multiple countries.
    It is assumed that the dataset has a 'country' column and each row
    corresponds to a different country with columns representing years.
    country (str): The name of the country for which the life expectancy
    projections will be plotted.

    Returns:
    None: This function does not return any value. It directly plots a graph
    showing the life expectancy projections for the specified country.

    Example:
    >>> import pandas as pd
    >>> import matplotlib.pyplot as plt
    >>> data = pd.read_csv('life_expectancy_projections.csv')
    >>> aff_life(data, 'United States')

    Notes:
    - The input DataFrame `data` should have a structure where each row
      represents a country and columns represent years with life expectancy
      values.
    - The 'country' column in the DataFrame should contain the names of the
      countries.
    - This function uses Matplotlib for plotting and assumes that the library
      is imported as `plt`.
    """
    country_data = data[data['country'] == country].transpose()
    country_data.columns = country_data.iloc[0]
    country_data = country_data.drop('country')
    country_data.index = country_data.index.astype(int)

    plt.plot(country_data)
    plt.title(country + ' Life Expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()


def main(argv):
    df = load(argv[1])
    country = argv[2]

    aff_life(df, country)


if __name__ == "__main__":
    main(sys.argv)

import sys
import matplotlib.pyplot as plt

from load_csv import load


def aff_pop(data, country, start_year=1800, end_year=2050):
    """
    Processes the population data for a given country and limits the years to a
    specified range.

    Parameters:
    data (pandas.DataFrame): The dataset containing population projections for
    multiple countries.
    It is assumed that the dataset has a 'country' column and each row
    corresponds to a different country with columns representing years.
    country (str): The name of the country for which the population data will
    be processed.
    start_year (int): The start year for the data range.
    end_year (int): The end year for the data range.

    Returns:
    pandas.DataFrame: A DataFrame with years as the index and population values
    as floats.
    """
    if country not in data['country'].values:
        raise ValueError(f"Country '{country}' not found in the dataset.")

    country_data = data[data['country'] == country].transpose()

    country_data.columns = country_data.iloc[0]
    country_data = country_data.drop(country_data.index[0])

    def convert_population(val):
        if isinstance(val, str) and val[-1] == 'k':
            return float(val[:-1]) * 1e3
        elif isinstance(val, str) and val[-1] == 'M':
            return float(val[:-1]) * 1e6
        return float(val)

    country_data = country_data.map(convert_population)

    country_data.index = country_data.index.astype(int)

    country_data = country_data[(country_data.index >= start_year)
                                & (country_data.index <= end_year)]

    return country_data


def plot_populations(data, country, country2):
    """
    Plots the population projections for two given countries based on the
    provided dataset.

    Parameters:
    data (pandas.DataFrame): The dataset containing population projections for
    multiple countries.
    It is assumed that the dataset has a 'country' column and each row
    corresponds to a different country with columns representing years.
    country (str): The name of the first country for which the population
    projections will be plotted.
    country2 (str): The name of the second country for which the population
    projections will be plotted.

    Returns:
    None: This function does not return any value. It directly plots a graph
    showing the population projections for the specified countries.
    """
    try:
        country_data = aff_pop(data, country)
        country2_data = aff_pop(data, country2)
    except ValueError as e:
        print(e)
        return

    plt.plot(country_data.index, country_data[country], label=country)
    plt.plot(country2_data.index, country2_data[country2], label=country2)
    plt.title(f'Population Projections: {country} vs {country2}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()


def main(argv):
    df = load("population_total.csv")
    country = "Brazil"
    country2 = "Mexico"

    plot_populations(df, country, country2)


if __name__ == "__main__":
    main(sys.argv)

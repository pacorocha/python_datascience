import sys
import matplotlib.pyplot as plt

from load_csv import load


def aff_life(data, country):
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

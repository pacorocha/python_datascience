import sys
import matplotlib.pyplot as plt

from load_csv import load


def main(argv):
    file1 = "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    file2 = "./life_expectancy_years.csv"
    year = argv[1]
    df_file1 = load(file1)
    df_file2 = load(file2)
    year_income = df_file1[year]
    life_expectancy_data = df_file2[year]

    plt.title(f'{year}')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.scatter(year_income, life_expectancy_data)
    plt.show()

if __name__ == "__main__":
    main(sys.argv)

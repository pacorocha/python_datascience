import sys
import matplotlib.pyplot as plt

from load_csv import load


def main(argv):
    try:
        if len(argv) < 2:
            raise ValueError("A year must be specified as an argument.")

        file1 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        file2 = "life_expectancy_years.csv"
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

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main(sys.argv)

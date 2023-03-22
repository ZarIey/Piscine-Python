import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import sys as check


def find_value(toto, char) -> bool:
    '''ratio'''
    index = np.where(toto == char)
    if index != -1:
        return 1
    return 0


def main():
    ''' main program, displays a chart of the population expectancy of
    two differents countries using the data from a csv file'''

    df = load("population_total.csv")
    print("Rentrez le premier pays a comparer: ")
    catch = check.stdin.readline().strip()
    print("Rentrez le deuxieme pays a comparer: ")
    catch2 = check.stdin.readline().strip()
    country1 = df.loc[df["country"] == catch]
    country2 = df.loc[df["country"] == catch2]
    country1 = country1.iloc[:, 1:252]
    country2 = country2.iloc[:, 1:252]
    x_title = "Year"
    y_title = "Population"
    toto = country1.to_numpy()
    if find_value(toto, "M") == 1:
        country2_population = country2.applymap(lambda x: float(x.strip("M")))
        country1_population = country1.applymap(lambda x: float(x.strip("M")))
    years = country1.columns.values.astype(int)
    mask = (years >= 1800) & (years <= 2050)

    fig, ax = plt.subplots()

    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)

    ax.plot(years[mask], country2_population.values[0][mask], label=catch2)
    ax.plot(years[mask], country1_population.values[0][mask], label=catch)

    # Set y-axis tick markse
    ax.set_yticks([20, 40, 60])
    ax.set_yticklabels(["20M", "40M", "60M"])

    plt.xticks(range(1800, 2041, 40))
    plt.title("Population Projections")
    plt.legend(loc="lower right")
    plt.show()

    return


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Only pays in M please ...")
        check.exit()

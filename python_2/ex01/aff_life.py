import matplotlib.pyplot as plt
from load_csv import load


def main():
    ''' main program, display a graphic from a .csv'''
    df = load("life_expectancy_years.csv")
    x_data = df.loc[df["country"] == "France"]
    y_data = x_data.iloc[:, 10:281]
    year = y_data.columns.values.astype(int)
    mask = (year > 1800) & (year < 2080)
    plt.plot(year[mask], y_data.values[0][mask])
    plt.xticks(range(1800, 2081, 40))
    plt.title('France life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    
    plt.show()


if __name__ == "__main__":
    main()

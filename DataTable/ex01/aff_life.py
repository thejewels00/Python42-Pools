import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(data, country):
    '''this function used to plot the contry information into a graph'''
    try :
        # extraction data
        country_data = data[data['country'] == country].iloc[0]
        years = country_data.index[1:]
        life_expectancy = country_data.values[1:]
        # ici je vais commencer le ploting
        plt.figure(figsize=(10, 5))
        plt.plot(years, life_expectancy)
        plt.title(f'Life Expectancy Projections in {country}')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.legend([country])
        plt.xticks(years[::20])
        # plt.legend([country])
        plt.show()
        plt.savefig(f"life_expectancy_{country}.png")
    except Exception as e:
        print(f"error in ploting: {e}")


if __name__ == "__main__":
    file_path = '../life_expectancy_years.csv'
    data = load(file_path)
    campus_country = "France"
    # print(data.columns)
    plot_life_expectancy(data, campus_country)
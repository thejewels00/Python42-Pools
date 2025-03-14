from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_projection(income_data, life_expectancy_data):
    '''making projection and plot :D'''
    try:
        # here i extract two columns :D
        income_in_1900 = income_data[['country', '1900']]
        life_exp_1900 = life_expectancy_data[['country', '1900']]
        # print("income ", income_in_1900)
        # print("life_exp ", life_exp_1900)
        merged_data = pd.merge(income_in_1900, life_exp_1900, on='country',
                               suffixes=('_income', '_life_exp'))
        # print(merged_data)
        plt.figure(figsize=(12, 8))
        # sns.scatterplot(data=merged_data, x='1900_income', y='1900_life_exp',
        #                 hue='country', palette='tab10')
        sns.scatterplot(data=merged_data, x='1900_income', y='1900_life_exp')
        plt.title('Projection of Life Expectancy in Relation to GNP in 1900')
        plt.xlabel('Gross National Product (GNP)')
        plt.ylabel('Life Expectancy')
        plt.show()
        plt.savefig('the_projection.png')
    except Exception as e:
        print(f"Error in plotting: {e}")


if __name__ == "__main__":
    path = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_expectancy_path = "../life_expectancy_years.csv"
    income_data = load(path)
    life_expectancy_data = load(life_expectancy_path)

    if income_data is not None and life_expectancy_data is not None:
        plot_projection(income_data, life_expectancy_data)

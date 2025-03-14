import matplotlib.pyplot as plt
from load_csv import load
import matplotlib.ticker as ticker
import numpy as np

def convert_population(pop_str):
    """Convertit une chaîne comme '29M' ou '534k' en nombre"""
    if not isinstance(pop_str, str):
        return pop_str
    
    pop_str = pop_str.strip()
    if pop_str.endswith('M'):
        return float(pop_str[:-1]) * 1000000
    elif pop_str.endswith('k'):
        return float(pop_str[:-1]) * 1000
    else:
        try:
            return float(pop_str)
        except:
            return 0

def plot_population(data, countries):
    '''this function used to plot the country information into a graph'''

    try:
        plt.figure(figsize=(12, 6))
        
        colors = ['#1f77b4', '#ff7f0e']  # Bleu et orange
        all_populations = []
        
        for i, country in enumerate(countries):
            country_data = data[data['country'] == country].iloc[0]
            years = country_data.index[1:]
            years = [year for year in years if 1800 <= int(year) <= 2050]
            
            population = [convert_population(country_data[year]) for year in years]
            all_populations.extend(population)
            
            plt.plot(years, population, label=country, color=colors[i])
        
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        
        plt.xticks(years[::20])
        
        max_pop = max(all_populations)
        min_pop = min(all_populations)
        
        y_values = np.linspace(min_pop, max_pop, 8)
        plt.yticks(y_values)
        
        def millions(x, pos):
            return f'{x/1e6:.1f}M'
        
        formatter = ticker.FuncFormatter(millions)
        plt.gca().yaxis.set_major_formatter(formatter)
        
        plt.legend()
        
        plt.savefig(f"population_{countries[0]}_{countries[1]}.png")
        plt.show()
        
    except Exception as e:
        print(f"error in plotting: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    file_path = '../population_total.csv'
    data = load(file_path)
    campus_country = ["France", "Belgium"]
    plot_population(data, campus_country)

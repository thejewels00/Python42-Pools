import pandas as pd

def load(path: str):
    ''' this function is useful to load csv dataset'''
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


if __name__ == "__main__":
    print(load("../life_expectancy_years.csv"))
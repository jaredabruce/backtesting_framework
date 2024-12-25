# data/data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.filepath, parse_dates=True, index_col='Date')
        self.data.sort_index(inplace=True)
        self.data.fillna(method='ffill', inplace=True)
        return self.data

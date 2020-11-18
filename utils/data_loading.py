import pandas as pd

class ZaloLoader:
    
    def __init__(self):
        self.data = []

    def read_csv(self, filepath):
        self.data = self.data.append(pd.read_csv(filepath))
        return self.data



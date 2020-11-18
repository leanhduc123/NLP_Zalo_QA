import pandas as pd

class ZaloLoader:
    
    def __init__(self):
        self.data = []

    def read_csv(self, filepath):
        self.data = self.data.append(pd.read_csv(filepath, encoding="ISO-8859-1"))
        return self.data

    def sum(self, a):
        print(a)



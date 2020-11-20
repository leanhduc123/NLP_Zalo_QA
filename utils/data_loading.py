import pandas as pd

class ZaloLoader:
    
    def __init__(self):
        self.data = pd.DataFrame(data={})

    def read_csv(self, filepath):
        self.data = self.data.append(pd.read_csv(filepath))
        return self.data
    def read_json(self, filepath):
        self.data = self.data.append(pd.read_json(filepath))
        return self.data



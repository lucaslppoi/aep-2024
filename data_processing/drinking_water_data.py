import pandas as pd

class DrinkingWaterData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        self.data = self.data.rename(columns={
            'Location': 'País',
            'Indicator': 'Indicador de Água',
            'Period': 'Ano',
            'First Tooltip': 'Percentual de Água'
        })

    def get_data(self):
        return self.data

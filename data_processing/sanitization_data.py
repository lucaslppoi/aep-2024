import pandas as pd

class SanitizationData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        self.data = self.data.rename(columns={
            'Location': 'País',
            'Indicator': 'Indicador de Saneamento',
            'Period': 'Ano',
            'Dim1': 'Tipo de População',
            'First Tooltip': 'Percentual de Saneamento'
        })

    def get_total_population_data(self):
        return self.data[self.data['Tipo de População'] == 'Total']

import DataEntry as DataEntry
import pandas as pd
import numpy as np

class Parameters: 
    def __init__(self, initialConcentration, maxConcentration, height):
        self.initialConcentration = initialConcentration
        self.height = height
        self.maxConcentration = maxConcentration

parameters = Parameters(0.1,0.3,5)
dataSheet = pd.read_csv("BKSP/Dataset.csv")
data = DataEntry.DataModel(dataSheet)
data.plot()
print(data.interpolate(0.1))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataModel:
    def __init__(self, dataSheet):
        self.fluxData = np.array(dataSheet["solidsFlux"])
        self.concentrationData = np.array(dataSheet["concentration"])

    def plot(self):
        plt.plot(self.concentrationData,self.fluxData)
        plt.show()

    def interpolate(self, concentration):
        return np.interp(concentration,self.concentrationData,self.fluxData)

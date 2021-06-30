import DataEntry as DataEntry
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Parameters: 
    def __init__(self, initialConcentration, maxConcentration, height):
        self.initialConcentration = initialConcentration
        self.height = height
        self.maxConcentration = maxConcentration


def OleinikCriteria(left_concentration,right_concentration,data):
    middlePoint = (left_concentration + right_concentration) / 2
    f_left = data.interpolate(left_concentration)
    f_right = data.interpolate(right_concentration)
    f_middle = data.interpolate(middlePoint)
    boundary = (f_right - f_left) / (right_concentration - left_concentration)
    lower_boundary = (f_middle - f_left) / (right_concentration - left_concentration)
    upper_boundary = (f_middle - f_right) / (left_concentration - right_concentration)
    return lower_boundary <= boundary and upper_boundary >= boundary

def InterfaceTrack(left_concentration,right_concentration,data):
    if OleinikCriteria(left_concentration,right_concentration,data):
        


parameters = Parameters(0.1,0.3,5)
dataSheet = pd.read_csv("BKSP/Dataset.csv")
data = DataEntry.DataModel(dataSheet)
# data.plot()
if OleinikCriteria(0,parameters.initialConcentration,data):
    f_0 = data.interpolate(0)
    f_phi = data.interpolate(parameters.initialConcentration)
    plt.plot([0,parameters.initialConcentration],[f_0, f_phi])

if OleinikCriteria(parameters.initialConcentration,parameters.maxConcentration,data):
    f_phi = data.interpolate(parameters.initialConcentration)
    f_phimax = data.interpolate(parameters.maxConcentration)
    plt.plot([parameters.initialConcentration,parameters.maxConcentration],[f_phi,f_phimax])
else:



plt.plot(data.concentrationData,data.fluxData)

plt.show()
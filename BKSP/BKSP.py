import DataEntry as DataEntry
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Parameters: 
    def __init__(self, initialConcentration, maxConcentration, height):
        self.initialConcentration = initialConcentration
        self.height = height
        self.maxConcentration = maxConcentration


class InterfaceTrack:
    def __init__(self,left_concentration,right_concentration,data):
        self.left_concentration = left_concentration
        self.right_concentration = right_concentration
        self.data = data

    

    def OleinikCriteria(self):
        self.middlePoint = (self.left_concentration + self.right_concentration) / 2
        self.f_left = self.data.interpolate(self.left_concentration)
        self.f_right = data.interpolate(self.right_concentration)
        self.f_middle = data.interpolate(self.middlePoint)
        boundary = (self.f_right - self.f_left) / (self.right_concentration - self.left_concentration)
        lower_boundary = (self.f_middle - self.f_left) / (self.right_concentration - self.left_concentration)
        upper_boundary = (self.f_middle - self.f_right) / (self.left_concentration - self.right_concentration)

        return lower_boundary <= boundary and upper_boundary >= boundary

    def DescreaseRightLimit(self):
        self.right_concentration -= 0.01

    def DecreaseLeftLimit(self):
        self.left_concentration -= 0.01

    def IncreaseLeftLimit(self):
        self.left_concentration += 0.01

    def SetLeftLimit(self,concentration):
        self.left_concentration = concentration

    def SetRightLimit(self,concentration):
        self.right_concentration = concentration

dataSheet = pd.read_csv("BKSP/Dataset.csv")
data = DataEntry.DataModel(dataSheet)
parameters = Parameters(0.1,0.3,5)  

upperInterface = InterfaceTrack(0,parameters.initialConcentration,data)
lowerInterface = InterfaceTrack(parameters.initialConcentration,parameters.maxConcentration,data)

if upperInterface.OleinikCriteria():
    #Caso 1
    plt.plot([0,parameters.initialConcentration],[upperInterface.f_left, upperInterface.f_right])

if lowerInterface.OleinikCriteria():
    #Caso 1
    plt.plot([parameters.initialConcentration,parameters.maxConcentration],[lowerInterface.f_left, lowerInterface.f_right])
else:
    #Caso 2 e 3
    hasFoundTan = False
    while(not hasFoundTan):
        if lowerInterface.right_concentration >= lowerInterface.left_concentration + 0.01:
            lowerInterface.IncreaseLeftLimit()
        else: 
            hasFoundTan = True
        if lowerInterface.OleinikCriteria():
            hasFoundTan = True
            plt.plot([lowerInterface.left_concentration,lowerInterface.right_concentration],[lowerInterface.f_left, lowerInterface.f_right])

    #Caso 2
    lowerInterface.SetLeftLimit(parameters.initialConcentration)
    hasFoundTan = False
    while(not hasFoundTan):
        lowerInterface.DescreaseRightLimit()
        if lowerInterface.OleinikCriteria():
            hasFoundTan = True
            plt.plot([lowerInterface.left_concentration,lowerInterface.right_concentration],[lowerInterface.f_left, lowerInterface.f_right])

print(lowerInterface.left_concentration)
plt.plot(data.concentrationData,data.fluxData)

plt.show()
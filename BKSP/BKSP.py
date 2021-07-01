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
parameters = Parameters(0.08,0.3,5)  

upperInterface = InterfaceTrack(0,parameters.initialConcentration,data)
lowerInterface = InterfaceTrack(parameters.initialConcentration,parameters.maxConcentration,data)

descSlope = 0
ascSlope1 = 0 #Implementar função de derivada
ascSlope2 = 0


if upperInterface.OleinikCriteria():
    #Caso 1
    plt.plot([upperInterface.left_concentration,upperInterface.right_concentration],[upperInterface.f_left, upperInterface.f_right])
    descSlope = upperInterface.f_right / upperInterface.right_concentration

if lowerInterface.OleinikCriteria():
    #Caso 1
    plt.plot([parameters.initialConcentration,parameters.maxConcentration],[lowerInterface.f_left, lowerInterface.f_right])
else:
    #Caso 2 e 3
    hasFoundTan = False
    while(not hasFoundTan):
        if lowerInterface.right_concentration > lowerInterface.left_concentration + 0.01:
            lowerInterface.IncreaseLeftLimit()
        else: 
            hasFoundTan = True
            f_0 = data.interpolate(lowerInterface.right_concentration)
            f_1 = data.interpolate(lowerInterface.right_concentration - 0.01)
            plt.plot([lowerInterface.right_concentration,lowerInterface.right_concentration - 0.1],[f_0,f_1])
            ascSlope2 = (f_1 - f_0) / 0.01
        if lowerInterface.OleinikCriteria():
            hasFoundTan = True
            plt.plot([lowerInterface.left_concentration,lowerInterface.right_concentration],[lowerInterface.f_left, lowerInterface.f_right])

    #Caso 2
    lowerInterface.SetLeftLimit(parameters.initialConcentration)
    hasFoundTan = False
    while(not hasFoundTan):
        if lowerInterface.right_concentration > lowerInterface.left_concentration + 0.01:
            lowerInterface.DescreaseRightLimit()
        else:
            hasFoundTan = True
            f_0 = data.interpolate(lowerInterface.left_concentration)
            f_1 = 2*data.interpolate(lowerInterface.left_concentration + 0.01) - 2*f_0
            plt.plot([lowerInterface.left_concentration,lowerInterface.left_concentration + 0.1],[f_0,f_1])
            ascSlope1 = (f_1 - f_0) / 0.01
        if lowerInterface.OleinikCriteria():
            hasFoundTan = True
            plt.plot([lowerInterface.left_concentration,lowerInterface.right_concentration],[lowerInterface.f_left, lowerInterface.f_right])

print(lowerInterface.left_concentration)
plt.plot(data.concentrationData,data.fluxData)

plt.show()

t1 = parameters.height / (ascSlope1 - descSlope)
z1 = descSlope * t1 + parameters.height
plt.plot([0,t1],[parameters.height,z1])
plt.plot([0,t1],[0,z1])

plt.show()
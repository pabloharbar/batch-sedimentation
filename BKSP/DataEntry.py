import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataSheet = pd.read_csv("BKSP/Dataset.csv")
fluxData = dataSheet["solidsFlux"]
concentrationData = dataSheet["concentration"]

plt.plot(concentrationData, fluxData)
plt.show()
# -*- coding: utf-8 --
"""
Created on Thu May  2 20:38:12 2019

@author: egwil
Script Name: Data Imports
"""

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt 
import pandas as pd

#dirStation = r'C:/Users/egwil/OneDrive/Desktop/tmpData/Stations.xls'
dirTemp = r'C:/Users/egwil/OneDrive/Desktop/tmpData/rainfall and temperature.xlsx'
#dirHumid = r'C:/Users/egwil/OneDrive/Desktop/tmpData/hum press wind (8 14 & 20).xlsx'


#dfStation = pd.read_excel(dirStation)
dfTemp = pd.read_excel(dirTemp)
#dfHumid = pd.read_excel(dirHumid)

#print(dfStation)
print(dirTemp)
#print(dirHumid)
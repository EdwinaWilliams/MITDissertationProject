# -*- coding: utf-8 --
"""
Created on Thu May  2 20:38:12 2019

@author: egwil
Script Name: Data Imports
"""

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns

dirTemp = r'C:/Users/egwil/OneDrive/Desktop/tmpData/rainfall and temperature.xlsx'

#one liner of code below: opsd_daily = pd.read_csv('opsd_germany_daily.csv', index_col=0, parse_dates=True)
dfTemp = pd.read_excel(dirTemp)
dfTemp = dfTemp.set_index('DateT')

#Add columns with year, month, and weekday name
dfTemp['Year'] = dfTemp.index.year
dfTemp['Month'] = dfTemp.index.month
dfTemp['Weekday Name'] = dfTemp.index.weekday_name

# Display a random sampling of 5 rows
#print(dfTemp.sample(5, random_state=0))

# Use seaborn style defaults and set the default figure size
#sns.set(rc={'figure.figsize':(20, 10)})

#dfTemp['MaxTemp (°C)'].plot(linewidth=0.5);

cols_plot = ['MaxTemp (°C)', 'MinTemp(°C)', 'Rain (mm)']
axes = dfTemp[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(20, 15), subplots=True)

for ax in axes:
    ax.set_ylabel('Daily Totals')
    
"""
Comm lines for meta data 
"""
# structure of data: # of rows, # of columns
#print(dfTemp.shape)

# First three and last three rows 
#print(dfTemp.head(3))
#print(dfTemp.tail(3))

# Checking data types (**make sure that date field that will be used for the time series)
#print(dfTemp.dtypes)

#Display index values 
#print(dfTemp.index)
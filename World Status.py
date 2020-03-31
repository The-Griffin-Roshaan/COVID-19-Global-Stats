# ©2020 Roshaan
import matplotlib
import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import reader
from pandas import DataFrame
from tabulate import tabulate
import math
import mplcursors

# Data Handling
file = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/worldwide-aggregated.csv")
table_list = file.values.tolist()
table_list[0][4] = 0


# Table
SHORT_HEADER = ['Date','Confirmed','Recovered','Deaths','Increase Rate'] 
table = tabulate(table_list,headers=SHORT_HEADER,tablefmt='fancy_grid')
print(table)

# Values Of Graph
x_axis_date = []
y_axis = []
y_value_cases = []
y_cure = []

for i in table_list:
    x_axis_date.append(i[0])
    y_value_cases.append(i[1])
    y_cure.append(i[2])

plt.figure(1)
plt.title('Cases Vs Cure')
line_1, = plt.plot(x_axis_date, y_value_cases, color='red', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='yellow', markersize=7)
line_2, = plt.plot(x_axis_date, y_cure, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=7)
plt.xticks(x_axis_date, rotation='vertical')
plt.xlabel('Date')
plt.ylabel('Cases')
line_1.set_label('Cases')
line_2.set_label('Cure')
plt.legend(loc='upper left')
mplcursors.cursor(hover=True)

plt.show()

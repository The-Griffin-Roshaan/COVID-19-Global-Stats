# ©2020 Roshaan
import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 

extract_contents = lambda row: [x.text.replace('\n','')for x in row]
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADER = ['SNo.','State','Indian-Confirmed','Foreign-Confirmed','Cured','Death']

response = requests.get(URL).content
soup = BeautifulSoup(response,'html.parser')
header = extract_contents(soup.tr.find_all('th'))

stats = []
all_rows = soup.find_all('tr')

for row in all_rows:
    stat = extract_contents(row.find_all('td'))

    if stat:
        if len(stat) == 5:
            #last row
            stat = ['',*stat]
            stats.append(stat)
        elif len(stat) == 6:
            stats.append(stat)

# Total

total_cases = []
cure_cases = []
death_cases = []


for row in stats:
    total_cases.append(int(row[3]))
    cure_cases.append(int(row[4]))
    death_cases.append(int(row[5]))
    

sum_total = 0 
cure_total = 0
death_total = 0

for no in total_cases:
    sum_total += no

for no in cure_cases:
    cure_total += no

for no in death_cases:
    death_total += no

stats.append([None,None,'Total Cases',sum_total,cure_total,death_total])

table = tabulate(stats,headers=SHORT_HEADER,tablefmt='fancy_grid')
print(table)
del stats[-1]




performance = []

for i in range(len(stats)):
    performance.append(int(stats[i][3])+int(stats[i][4]))

objects = []
for row in stats:
    objects.append(row[2])

y_pos = np.arange(len(objects))

b1 = plt.barh(y_pos,performance,align='center',alpha=1,color=(255/256.0, 28/256.0,123/256.0),edgecolor=(0,0,0))

plt.yticks(y_pos,objects)
#plt.xlim(0,300)
plt.xlabel('Number Of Cases')
plt.title('Corona Virus Cases')
plt.legend([b1], ["Cases"],loc= 'upper right')
plt.show()

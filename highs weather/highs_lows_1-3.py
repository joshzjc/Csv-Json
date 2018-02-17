import csv
from matplotlib import pyplot as plt

filename= 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(f)

    highs = [int(row[1]) for row in reader]
plt.figure(dpi = 128,figsize =(10,5))
plt.plot(highs,c='pink')
plt.title('Daily high temperatures,July 2014',fontsize = 24)
plt.xlabel('',fontsize = 16)
plt.ylabel('Temperature(F)',fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize = 16)
plt.savefig('highs weather.png')
plt.show()
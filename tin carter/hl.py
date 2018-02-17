import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename= 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,hights,lows = [],[],[]
    for row in reader:
        current_dates = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_dates)
        hight = int(row[1])
        hights.append(hight)
        low = int(row[3])
        lows.append(low)
#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,5))
plt.plot(dates,hights,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,hights,lows,facecolor = 'blue',alpha = 0.1)
plt.title('Daily high and low temperatures - 2014',fontsize = 24)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize = 16)
plt.show()




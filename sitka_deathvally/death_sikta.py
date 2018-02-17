import csv
from matplotlib import pyplot as plt
from datetime import datetime

def get_data(filename,dataes,heights,lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_dataes = datetime.strptime(row[0],'%Y-%m-%d')
                height = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_dataes,'missing data')
            else:
                dataes.append(current_dataes)
                heights.append(height)
                lows.append(low)

dataes,heights,lows = [],[],[]
get_data('sitka_weather_2014.csv',dataes,heights,lows)
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dataes,heights,c='red',linewidth = 2,alpha=0.6)
plt.plot(dataes,lows,c='blue',linewidth =2,alpha = 0.6)
plt.fill_between(dataes,heights,lows,facecolor = 'blue',alpha = 0.15)


dataes,heights,lows = [],[],[]
get_data('death_valley_2014.csv',dataes,heights,lows)
plt.plot(dataes,heights,c='pink',linewidth =2,alpha=0.6)
plt.plot(dataes,lows,c='purple',linewidth =2,alpha = 0.6)
plt.fill_between(dataes,heights,lows,facecolor = 'green',alpha = 0.05)


plt.title('Daily high and low temperatures - 2014\nSitka, AK and Death Valley, CA')
plt.xlabel('',fontsize = 12)
fig.autofmt_xdate()
plt.ylabel('Temperatuer(F)',fontsize = 12)
plt.tick_params(axis='both',which='major',labelsize = 12)
plt.ylim(10,120)
plt.show()
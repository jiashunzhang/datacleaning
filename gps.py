import sys

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(r"lib")
from gps_util import calc_distance

#gps = pd.read_csv('gps_20161101')
#print(gps[0])
def app():
    i = 0
    driverid = 'a'
    gpslist = []
    speed_list = []
    with open('gps_20161103') as gps:
        for line in gps:
            i = i+1  # 每行末尾会有一个换行符
            speed = pd.Series(line.strip('\n').split(','))
            if i == 1:
                driverid = speed[0]
            if speed[0] != driverid:
                break
            else:
                gpslist.append([(float)(speed[2]), (float)(speed[3]), (float)(speed[4])])

    for index in range(len(gpslist)):
        if index > 0:
            distance = calc_distance(gpslist[index-1][1], gpslist[index-1][2], gpslist[index][1], gpslist[index][2])
            speed = distance / (gpslist[index][0]-gpslist[index-1][0])
            speed_list.append(speed)

    print(speed_list)
    x_axis = range(0, len(speed_list), 1)
    plt.plot(x_axis, speed_list)
    plt.ylabel('速度 (m/s)', fontproperties='SimHei', fontsize=15)
    plt.xlabel('时间 (s)', fontproperties='SimHei', fontsize=15)
    plt.show()
app()

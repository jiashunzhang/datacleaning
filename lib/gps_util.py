'''本文件用于gps辅助工具'''

import math

PI = 3.1415926535898
EARTH_RADIUS = 6378.137

def rad(angular):
    return angular * PI / 180.0


def calc_distance(lati1, long1, lati2, long2):
    ''' 计算两gps坐标点之间的距离'''
    rad_lat1 = rad(lati1)
    rad_lat2 = rad(lati2)
    lat_diff = rad_lat1 - rad_lat2
    long_diff = rad(long1) - rad(long2)
    distance = 2 * math.asin(math.sqrt(pow(math.sin(lat_diff/2), 2) + math.cos(rad_lat1)*math.cos(rad_lat2)*math.pow(math.sin(long_diff/2), 2)))
    distance = distance * EARTH_RADIUS
    distance = (int)(distance * 10000000) / 10000
    return distance

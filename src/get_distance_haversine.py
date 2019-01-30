#!/usr/bin/python3

from math import sin, asin, cos, radians, fabs, sqrt

EARTH_RADIUS = 6371  # 地球平均半径，6371km


def haversine(theta):
    s = sin(theta / 2)
    return s * s

def get_distance_haversine(lat0, long0, lat1, long1):
    print('lat0=', lat0)
    print('lng1=', long1)
    """
    纬度：latitude
    经度：longitude
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 用haversine公式计算球面两点间的距离
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    long0 = radians(long0)
    long1 = radians(long1)

    dlng = fabs(long0 - long1)
    dlat = fabs(lat0 - lat1)
    h = haversine(dlat) + cos(lat0) * cos(lat1) * haversine(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance

# test
lat1, lon1 = (22.599578, 113.973129)  # 深圳野生动物园(起点）
lat2, lon2 = (22.6986848, 114.3311032)  # 深圳坪山站 (百度地图测距：38.3km)
print(lon1)
d2 = get_distance_haversine(lat1, lon1, lat2, lon2 )
print(d2)

lat2, lon2 = (39.9087202, 116.3974799)  # 北京天安门(1938.4KM)
d2 = get_distance_haversine(lat1,lon1, lat2,lon2 )
print(d2)


dist = get_distance_haversine(120.147118, 30.278594, 121.490807, 31.222471);
# hangzhou xihu 30.278594,120.147118
# shanghai 31.222471,121.490807
print(dist)
import requests
import xml.etree.ElementTree as ET
import json

global key
global drivingUrl
key = '9b4e518115da0b6534ae3abf1edc0186'
drivingUrl = 'https://restapi.amap.com/v3/direction/driving?origin={}&destination={}&roadaggregation=true&extension=all&output=json&key=' + key
print(drivingUrl)


def getDP(origin: list, destination: list) -> list:
    '''
    origin: list of origin coordinate
    destination: list of destation coordinate

    This method sends one navigation request based on the origin and destination.
    '''
    url = drivingUrl.format(
        str(origin[0]) + ',' + str(origin[1]),
        str(destination[0]) + ',' + str(destination[1]))
    res = requests.get(url)
    resInfo = json.loads(res.text)
    return resInfo['route']['paths'][0]['roads']


def coordUtil(tmc: list, roadName: str, orientation: str) -> list:
    '''
    tmc: List of route latitude and longitude

    This method is used to split a list of path points into a list of line segments.
    '''
    n = len(tmc)
    pairList = []
    for i in range(n - 1):
        pairList.append({
            'road_unit_head': tmc[i],
            'road_unit_tail': tmc[i + 1],
            'road_name': roadName,
            'orientation': orientation,
            'action': '直行',
            'distence': 0})
    return pairList


def getRoadObj(OR: list, DE: list) -> dict:
    '''
    OR: list of origin coordinate
    DE: list of destation coordinate

    This method is used to get the road object from a single Highlander navigation request.
    '''
    roadstep = getDP(OR, DE)  # 通过高德api获取规划信息
    roadNum = len(roadstep)  # 获取规划涉及道路数量
    # roadstep[roadNum - 1]['steps']
    roadDict = dict()  # 初始化最终返回值道路字典，字典的键为道路名，值为线段列表
    pointNumTable = []  # 初始化每个tmc线段数量列表
    road_unit_set = []
    for road_index, road in enumerate(roadstep): # 每个道路循环
        roadName = road['road_name'] if road['road_name'] else "无名道路"
        print(roadName)
        roadPointList = []
        for tmc_index, tmcs in enumerate(road['steps']):
            orientation = tmcs['orientation']
            action = tmcs['action']
            for tmc in tmcs['tmcs']:
                ployline = tmc['polyline']
                pointList = ployline.split(';')
                pointList = coordUtil(pointList, roadName, orientation)
                roadPointList = roadPointList + pointList
                pointNumTable.append(len(pointList))
        if road_index == 0:
            roadPointList = roadPointList[pointNumTable[0]:]
        elif road_index == roadNum - 1:
            roadPointList = roadPointList[:-pointNumTable[-1]]
        roadDict[roadName] = roadPointList[:]
        road_unit_set = road_unit_set + roadPointList[:]
    return complete_line(road_unit_set)


def complete_line(road_set):
    for i in range(len(road_set) - 1):
        if road_set[i]['road_unit_tail'] != road_set[i+1]['road_unit_head']:
            road_set.insert(i+1, {
                'road_unit_head': road_set[i]['road_unit_tail'],
                'road_unit_tail': road_set[i+1]['road_unit_head'],
                'road_name': road_set[i]['road_name'],
                'orientation': road_set[i]['orientation'],
                'action': '转弯',
                'distence': 0})
    return road_set


if __name__ == "__main__":
    # OR = [125.326451, 43.803335]
    # DE = [125.324237, 43.951226]
    OR = [125.326451, 43.803335]
    DE = [125.347451, 43.803635]
    print(getRoadObj(OR, DE))

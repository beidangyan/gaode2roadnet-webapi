from . import getCoord
from Dao.roadMapper import RoadMapper
from Dao.duplicate import Duplicate


class RoadGetService:

    road_mapper = None

    def __init__(self):
        self.road_mapper = RoadMapper()

    def getRoadUnits(self, OR: list, DE: list):
        road_units = getCoord.getRoadObj(OR, DE)
        return road_units

    def saveAllRoadUnits(self, road_units):
        self.road_mapper.addAllRoadUnit(road_units)
        Duplicate.duplicateBaseData()

    def selectAllRoadUnits(self):
        resutl = self.road_mapper.getAllRoadUnits()
        print("所有请求已获取")
        return resutl

    def delete_all_road_data(self):
        self.road_mapper.delete_all_road_units()

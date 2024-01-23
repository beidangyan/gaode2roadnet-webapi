from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DB_URI
from models import RoadUnit
import json


class RoadMapper:
    session = None
    engine = create_engine(DB_URI)

    def __init__(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def addAllRoadUnit(self, road_units):
        """

        :param road_units:
        :return:
        """
        try:
            self.session.execute(RoadUnit.__table__.insert(), road_units)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("插入全部道路单元数据时发生错误")
        finally:
            self.session.close()


    def getAllRoadUnits(self):
        """
        :return: json of All Road Units
        :return:
        """
        result = []
        query_result = self.session.query(RoadUnit).all()
        for item in query_result:
            result.append(item.to_dict())
        self.session.close()
        return result

    def delete_all_road_units(self):
        try:
            self.session.query(RoadUnit).delete()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e, '删除所有数据时发生错误')
        finally:
            self.session.close()

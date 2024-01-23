from sqlalchemy import Column, Integer, String, create_engine, func
from config import DB_URI
from sqlalchemy.orm import sessionmaker
from models import RoadUnit


class Duplicate:
    engine = create_engine(DB_URI)
    session = sessionmaker(bind=engine)()

    def __init__(self):
        pass

    @staticmethod
    def duplicateBaseData():
        duplicate_groups = (
            Duplicate.session.query(RoadUnit.road_unit_head, RoadUnit.road_unit_tail, func.count().label('dup_count'))
            .group_by(RoadUnit.road_unit_head, RoadUnit.road_unit_tail)
            .having(func.count() > 1)
            .all()
        )
        for field1_val, field2_val, dup_count in duplicate_groups:
            # 保留ID最小的条目并删除其他所有条目
            min_id = (
                Duplicate.session.query(func.min(RoadUnit.id))
                .filter(RoadUnit.road_unit_head == field1_val, RoadUnit.road_unit_tail == field2_val)
                .scalar()
            )
            Duplicate.session.query(RoadUnit).filter(
                RoadUnit.road_unit_head == field1_val,
                RoadUnit.road_unit_tail == field2_val,
                RoadUnit.id != min_id  # 不是我们要保留的那个条目
            ).delete(synchronize_session=False)  # 避免在删除时刷新会话中的对象；这可以提高性能

        Duplicate.session.commit()
        Duplicate.session.close()

from exts import db


class RoadUnit(db.Model):
    __tablename__ = 'road_units'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    road_name = db.Column(db.String(10), nullable=False)
    road_unit_head = db.Column(db.String(20), nullable=False)
    road_unit_tail = db.Column(db.String(20), nullable=False)
    orientation = db.Column(db.String(10), nullable=False)
    action = db.Column(db.String(10), nullable=False)
    distence = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'road_name': self.road_name,
            'road_unit_head': self.road_unit_head,
            'road_unit_tail': self.road_unit_tail,
            'orientation': self.orientation,
            'action': self.action,
            'distance': self.distence
        }
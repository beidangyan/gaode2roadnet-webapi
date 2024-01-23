class RoadUnit:
    roadName = '未定义'
    roadUnitHead = ''
    roadUnitTail = ''
    orientation = ''
    action = ''

    def __init__(self, roadName: str, roadUnitPair: list, orientation: str, action: str) -> None:
        self.roadName = roadName
        self.roadUnitHead = roadUnitPair[0]
        self.roadUnitTail = roadUnitPair[1]
        self.orientation = orientation
        self.action = action

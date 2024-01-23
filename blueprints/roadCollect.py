import json

from flask import Blueprint, request, Response, jsonify
from Service import roadGetService
from utils import standardResponse
bp = Blueprint("roadCollect", __name__, url_prefix="/")


@bp.route("/")
def hello():
    return 'hello'


@bp.route("/saveRoad/", methods=["GET"])
def getRoadCollect():
    OR = request.args.get("OR").split(',')
    DE = request.args.get("DE").split(',')
    road_geter = roadGetService.RoadGetService()
    road_units = road_geter.getRoadUnits(OR, DE)
    road_geter.saveAllRoadUnits(road_units)
    return standardResponse.HttpResponse.success()


@bp.route("/getRoad/", methods=["GET"])
def getRoad():
    result_getter = roadGetService.RoadGetService()
    result = result_getter.selectAllRoadUnits()
    data = json.dumps(result, ensure_ascii=False)
    response = Response(data, mimetype='application/json')
    return response


@bp.route("/deleteAll/", methods=["GET"])
def delete_all():
    try:
        server = roadGetService.RoadGetService()
        server.delete_all_road_data()
        response = Response("删除成功", status=200)
    except Exception as e:
        response = Response("服务器处理请求时出错:"+str(e), status=500)
    finally:
        return response

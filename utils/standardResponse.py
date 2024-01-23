import json
from http import HTTPStatus


class HttpResponse:
    def __init__(self, json_data=None):
        pass

    @staticmethod
    def success(json_data=''):
        """
        生成成功的HTTP响应
        """
        status_code = HTTPStatus.OK
        message = "Success"
        response = {
            'status_code': status_code.value,
            'message': message,
            'Content-Type': 'text/html;charset=UTF-8',
        }
        if json_data:
            response['data'] = json_data
        return response

    @staticmethod
    def error(json_data=''):
        """
        生成错误的HTTP响应
        """
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        message = "Error"
        response = {
            'status_code': status_code.value,
            'message': message,
            'Content-Type': 'text/html;charset=UTF-8',
        }
        if json_data:
            response['data'] = json_data
        return response

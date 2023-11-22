from flask_restful import Resource
from dataclasses import dataclass, asdict
from functools import wraps
import threading
import uuid
from app.webserver.logger import ServerLogContent, slogger, rlogger
from flask import request


@dataclass
class ResponseJson:
    data: any
    code: int
    message: str = ''

    def to_dict(self):
        return asdict(self), self.code


class HandlerFuncs:

    @staticmethod
    def auth_handler(func):
        rlogger.info('auth')

        @wraps(func)
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return x

        return wrapper

    @staticmethod
    def param_handler(func):
        rlogger.info('params')

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def get_handler_funcs(cls):
        ls = [cls.auth_handler, cls.param_handler]
        return ls[::-1]

    @staticmethod
    def error_exception_handler(error):
        rlogger.error(str(error))
        error_message = str(error)
        return ResponseJson(data='', code=500, message=error_message).to_dict()

    @staticmethod
    def error_404_handler(error):
        rlogger.error('Not Found')
        slogger.info(ServerLogContent(action='response', code=404, error_message='Resource Not Found').to_dict())
        return ResponseJson(data='', code=404, message=str(error)).to_dict()

    @staticmethod
    def after_handler(response):
        rlogger.info(f'{threading.current_thread().name} {response.status_code}')
        if response.status_code == 200:
            slogger.info(ServerLogContent(action='response', code=response.status_code).to_dict())
        return response

    @staticmethod
    def before_handler():
        request_id = uuid.uuid4().hex
        threading.current_thread().name = request_id

        rlogger.info(f'request ID: {request_id}')
        rlogger.info(f'{request.method} {request.path} {request.remote_addr}')
        rlogger.info(f'authorization: {request.authorization}')

        slogger.info(ServerLogContent(action='receive').to_dict())


class ServiceHandler(Resource):
    method_decorators = HandlerFuncs.get_handler_funcs()

    @staticmethod
    def output(data, dtype='json', code=200, message=''):

        match dtype:
            case 'json':
                return ResponseJson(data, code, message).to_dict()
            case 'text':
                return data, code, {'Content-Type': 'text/plain'}
            case _:
                return data, code, {'Content-Type': 'application/json'}

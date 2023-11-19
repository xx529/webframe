from flask_restful import Resource
from dataclasses import dataclass, asdict
from functools import wraps
import threading
import uuid
from app.appserver.logger import logger
import random


@dataclass
class ResponseJson:
    data: any
    code: int
    message: str = ''

    def to_dict(self):
        return asdict(self), self.code


class HandlerFuncs:

    @staticmethod
    def log_start_handler(func):
        @wraps(func)
        def start_log(*args, **kwargs):
            logger.info(f'log start')
            return func(*args, **kwargs)

        return start_log

    @staticmethod
    def auth_handler(func):
        @wraps(func)
        def auth(*args, **kwargs):
            logger.info('auth')
            x = func(*args, **kwargs)
            return x

        return auth

    @staticmethod
    def param_handler(func):
        @wraps(func)
        def params(*args, **kwargs):
            logger.info('param')
            if random.random() > 0.5:
                return ResponseJson(data='', code=400, message='param fail').to_dict()
            else:
                return func(*args, **kwargs)

        return params

    @classmethod
    def get_handler_funcs(cls):
        ls = [cls.log_start_handler,
              cls.auth_handler,
              cls.param_handler]
        return ls[::-1]

    @staticmethod
    def error_exception_handler(error):
        logger.error(str(error))
        error_message = str(error)
        return ResponseJson(data='', code=500, message=error_message).to_dict()

    @staticmethod
    def error_404_handler(error):
        logger.error('Not Found')
        return ResponseJson(data='', code=404, message=str(error)).to_dict()

    @staticmethod
    def after_request_handler(response):
        print(type(response))
        return response

    @staticmethod
    def before_request_handler():
        threading.current_thread().name = uuid.uuid4().hex


class ServiceHandler(Resource):
    URL: str
    method_decorators = HandlerFuncs.get_handler_funcs()

    @staticmethod
    def response(data, dtype='json', code=200):

        match dtype:
            case 'json':
                return ResponseJson(data, code).to_dict()
            case 'text':
                return data, code, {'Content-Type': 'text/plain'}
            case _:
                return data, code, {'Content-Type': 'application/json'}

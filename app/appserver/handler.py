from flask_restful import Resource
from dataclasses import dataclass, asdict
from functools import wraps
import threading
import uuid


@dataclass
class ResponseJson:
    data: dict
    code: int
    message: str = ''

    def to_dict(self):
        return asdict(self)


class HandlerFuncs:

    @staticmethod
    def thread_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threading.current_thread().name = uuid.uuid4().hex
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def log_start_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            threading.current_thread().name = uuid.uuid4().hex
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def auth_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('auth')
            x = func(*args, **kwargs)
            print(x, 1)
            return x

        return wrapper

    @staticmethod
    def param_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('param')
            x = func(*args, **kwargs)
            print(x, 2)
            return x

        return wrapper

    @classmethod
    def get_handler_funcs(cls):
        return [cls.thread_handler, cls.log_start_handler, cls.auth_handler, cls.param_handler][::-1]


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

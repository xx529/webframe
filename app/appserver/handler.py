from flask_restful import Resource
from dataclasses import dataclass, asdict


@dataclass
class ResponseJson:
    data: dict
    code: int
    message: str = ''

    def to_dict(self):
        return asdict(self)


class ServiceHandler(Resource):
    URL: str

    @staticmethod
    def response(data, dtype='json', code=200):

        match dtype:
            case 'json':
                return ResponseJson(data, code).to_dict()
            case 'text':
                return data, code, {'Content-Type': 'text/plain'}
            case _:
                return data, code, {'Content-Type': 'application/json'}


class RequestHandler:
    pass

import datetime
import threading
from dataclasses import asdict, dataclass

from flask import request
from loguru import logger
from app.appserver.config import AppConf, LogConf
import sys

logger.remove()

# 运行日志记录到文件
logger.add(sink=LogConf.RUNTIME_FILE,
           format=LogConf.RUNTIME_FORMAT,
           level='INFO',
           filter=lambda x: x['extra']['name'] == 'runtime')

# 运行日志记录到标准输出
logger.add(sink=sys.stdout,
           format=LogConf.STDOUT_FORMAT,
           level='INFO',
           filter=lambda x: x['extra']['name'] == 'runtime')

# 服务请求日志
logger.add(sink=LogConf.SERVER_FILE,
           format=LogConf.SERVER_FORMAT,
           level='INFO',
           filter=lambda x: x['extra']['name'] == 'server')


rlogger = logger.bind(name='runtime')
slogger = logger.bind(name='server')


@dataclass
class ServerLogContent:
    action: str
    url: str = ''
    method: str = ''
    authorization: str = ''
    datetime: str = ''
    remote_addr: str = ''
    code: int = -1
    rid: str = ''
    frid: str = 'main'
    error_message: str = ''
    traceback: str = ''
    version: str = AppConf.VERSION

    def __post_init__(self):
        self.datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.authorization = str(request.authorization)
        self.url = request.path
        self.method = request.method
        self.remote_addr = request.remote_addr
        self.rid = threading.current_thread().name

    def to_dict(self):
        return asdict(self)

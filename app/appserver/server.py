from flask import Flask
from flask_restful import Api
from app.appserver.config import Dir, ConfigureFile, AppConf
from datetime import datetime
import sys
import psutil
from app.appserver.handler import Service


class Server:
    def __init__(self, name, host=None, port=None, debug=None):
        self.app = Flask(name)
        self.host = host or AppConf.HOST
        self.port = port or AppConf.PORT
        self.debug = debug if debug is not None else AppConf.DEBUG

    def run(self):
        self.init_dirs()
        self.add_services()
        self.server_info()
        self.app.run(host=self.host, port=self.port, debug=self.debug)

    def add_services(self):
        api = Api(self.app)
        for s in Service.__subclasses__():
            api.add_resource(s, f'{AppConf.PROJECT_PREFIX}{s.URL}')

    @staticmethod
    def init_dirs():
        check_dirs = [Dir.DATA, Dir.LOG]
        for d in check_dirs:
            if not d.exists():
                d.mkdir(parents=True)

    @staticmethod
    def server_info():
        print(f"""
    ######################### Server Info #########################
    | python    | {sys.version}
    | platform  | {sys.platform}
    | cpus      | {psutil.cpu_count()}
    | start     | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    | root      | {Dir.ROOT}
    | data      | {Dir.DATA}
    | log       | {Dir.LOG}
    | .env      | {ConfigureFile.ENV}
    ###############################################################
        """)

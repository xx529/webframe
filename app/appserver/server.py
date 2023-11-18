from flask import Flask
from app.appserver.config import Dir, ConfigureFile
from datetime import datetime
import sys
import psutil


class Server:
    def __init__(self, name, host='0.0.0.0', port=9938, debug=True):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.debug = debug

    def run(self):
        self.init_dirs()
        self.add_routers()
        self.server_info()
        self.app.run(host=self.host, port=self.port, debug=self.debug)

    def add_routers(self):
        pass

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

from flask import Flask
from flask_restful import Api
from flask_apscheduler import APScheduler
from app.resource.config import Dir, FilePath, ServerConf
from datetime import datetime
import sys
import psutil
from app.webserver.handler import HandlerFuncs


class Server:
    def __init__(self, name, host=None, port=None, debug=None):
        self.app = Flask(name)
        self.scheduler = APScheduler()
        self.api = Api(self.app, prefix=ServerConf.PROJECT_PREFIX)
        self.host = host or ServerConf.HOST
        self.port = port or ServerConf.PORT
        self.debug = debug if debug is not None else ServerConf.DEBUG

    def run(self):
        self.init_dirs()
        self.init_db()
        self.import_services()
        self.add_handlers()
        self.add_scheduler()
        self.server_info()
        self.app.run(host=self.host, port=self.port, debug=self.debug)

    def import_services(self):
        pass

    def add_handlers(self):
        self.app.errorhandler(Exception)(HandlerFuncs.error_exception_handler)
        self.app.errorhandler(404)(HandlerFuncs.error_404_handler)
        self.app.before_request(HandlerFuncs.before_handler)
        self.app.after_request(HandlerFuncs.after_handler)

    def add_scheduler(self):
        self.scheduler.init_app(self.app)
        self.scheduler.start()

    def init_db(self):
        pass

    @staticmethod
    def init_dirs():
        check_dirs = [Dir.DATA, Dir.LOG]
        for d in check_dirs:
            if not d.exists():
                d.mkdir(parents=True)

    @property
    def count_urls(self):
        return len(list(self.app.url_map.iter_rules()))

    def server_info(self):
        print(f"""
    ######################### Version {ServerConf.VERSION} #########################
    | python    | {sys.version}
    | platform  | {sys.platform}
    | cpus      | {psutil.cpu_count()}
    | start     | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    | urls      | {self.count_urls}
    | prefix    | {ServerConf.PROJECT_PREFIX}
    | root      | {Dir.ROOT}
    | data      | {Dir.DATA}
    | log       | {Dir.LOG}
    | .env      | {FilePath.ENV}
    ################################################################
        """)

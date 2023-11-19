import pathlib


class Dir:
    ROOT = pathlib.Path(__file__).parent.parent.parent
    SRC = ROOT / 'app'
    DATA = ROOT / 'data'
    LOG = DATA / 'log'
    RESOURCE = ROOT / 'resource'


class AppConf:
    HOST = '0.0.0.0'
    PORT = '9938'
    DEBUG = True
    PROJECT_PREFIX = '/hang'


class LogConf:
    RUNTIME_FILE = Dir.LOG / 'runtime.log'
    RUNTIME_FORMAT = '{time:HH:mm:ss.SSS} - {file} - {function}() - {line} - [{thread.name}] - {level} - {message}'
    SERVER_FILE = Dir.LOG / 'server.log'


class ConfigureFile:
    ENV = Dir.ROOT / '.env'

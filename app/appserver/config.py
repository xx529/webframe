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


class ConfigureFile:
    ENV = Dir.ROOT / '.env'

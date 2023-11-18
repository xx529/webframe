import pathlib


class Dir:
    ROOT = pathlib.Path(__file__).parent.parent.parent
    SRC = ROOT / 'app'
    DATA = ROOT / 'data'
    LOG = DATA / 'log'
    RESOURCE = ROOT / 'resource'


class AppConf:
    pass


class ConfigureFile:
    ENV = Dir.ROOT / '.env'

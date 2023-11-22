import pathlib


class Dir:
    ROOT = pathlib.Path(__file__).parent.parent.parent
    SRC = ROOT / 'app'
    DATA = ROOT / 'data'
    LOG = DATA / 'log'
    RESOURCE = ROOT / 'resource'


class ServerConf:
    VERSION = '1.0.0'
    HOST = '0.0.0.0'
    PORT = '9938'
    DEBUG = True
    PROJECT_PREFIX = '/hang'


class Log:
    RUNTIME_FILE = Dir.LOG / 'runtime.log'
    SERVER_FILE = Dir.LOG / 'server.log'

    RUNTIME_FORMAT = '{time:YYYY-MM-DD HH:mm:ss.SSS} - [{thread.name}] - {file} - {function}() - {line} - {level} - {message}'
    STDOUT_FORMAT = '{time:HH:mm:ss.SSS} | {level:<8} | {file}:{function}():{line} | {message}'
    SERVER_FORMAT = '{message}'

    console_format = '{time:HH:mm:ss.SSS} | {level:<8} | {file}:{function}():{line} | {message}'


class FilePath:
    ENV = Dir.ROOT / '.env'

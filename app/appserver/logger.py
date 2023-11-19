from loguru import logger
from app.appserver.config import LogConf
import sys

logger.remove()
logger.add(sink=LogConf.RUNTIME_FILE,
           format=LogConf.RUNTIME_FORMAT,
           level='INFO')

logger.add(sink=sys.stdout,
           format=LogConf.RUNTIME_FORMAT,
           level='INFO')

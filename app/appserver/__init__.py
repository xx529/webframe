from app.appserver.server import Server
from app.appserver.handler import ServiceHandler
from app.appserver.logger import rlogger

server = Server('myapp')
scheduler = server.scheduler
api = server.api.resource
log = rlogger

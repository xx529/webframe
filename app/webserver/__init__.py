from app.webserver.server import Server
from app.webserver.handler import ServiceHandler
from app.webserver.logger import rlogger

server = Server('myapp')
scheduler = server.scheduler
api = server.api.resource
log = rlogger

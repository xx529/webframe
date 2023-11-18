from app.appserver import Service


class HelloWorld(Service):
    URL = '/hello'

    def get(self):
        return {'ok': 'get'}, 200

    def post(self):
        return {'ok': 'post1'}, 200

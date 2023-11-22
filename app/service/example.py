from app.webserver import api, ServiceHandler

PREFIX = '/example'


@api(f'{PREFIX}/crud')
class ExampleCRUD(ServiceHandler):

    def get(self):
        return self.output(data='get', code=200)

    def post(self):
        return self.output(data='post', code=200)

    def put(self):
        return self.output(data='put', code=200)

    def delete(self):
        return self.output(data='delete', code=200)

    def patch(self):
        return self.output(data='delete', code=200)


@api(f'{PREFIX}/crud2')
class ExampleCRUD2ForGet(ServiceHandler):

    def get(self):
        return self.output(data='get', code=200)


@api(f'{PREFIX}/crud2')
class ExampleCRUD2ForPost(ServiceHandler):

    def post(self):
        return self.output(data='post', code=200)

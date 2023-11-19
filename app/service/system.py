from app.appserver import ServiceHandler
from app.appserver import server, log
import pandas as pd


class HelloWorld(ServiceHandler):
    URL = '/hello'

    def get(self):
        return {'ok': 'get'}, 200

    def post(self):
        return {'ok': 'post1'}, 200

    def delete(self):
        return {'ok': 'delete'}, 200


class ShowUrls(ServiceHandler):

    URL = '/system/urls'

    def get(self):
        log.info('start server')
        rules = server.app.url_map.iter_rules()
        df_urls = pd.DataFrame([{'url': rule.rule, 'methods': ', '.join(sorted(rule.methods))} for rule in rules])
        df_urls.sort_values('url', inplace=True)
        data = df_urls.to_dict(orient='records')
        return self.response(data, code=200)

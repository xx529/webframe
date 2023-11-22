from app.webserver import ServiceHandler, server, log, api
from app.resource.config import Log
import pandas as pd

PREFIX = '/system'


@api(f'{PREFIX}/urls')
class AllUrls(ServiceHandler):

    def get(self):
        log.info('start server')
        rules = server.app.url_map.iter_rules()
        df_urls = pd.DataFrame([{'url': rule.rule, 'methods': ', '.join(sorted(rule.methods))} for rule in rules])
        df_urls.sort_values('url', inplace=True)
        data = df_urls.to_dict(orient='records')
        return self.output(data, code=200)


@api(f'{PREFIX}/log')
class ServerLog(ServiceHandler):

    def get(self):
        with open(Log.SERVER_FILE, 'r') as f:
            lines = [eval(x) for x in f.readlines()]

        df_log = pd.DataFrame(lines)
        return self.output(df_log.to_dict(orient='records'))


@api(f'{PREFIX}/log/<request_id>')
class RuntimeLog(ServiceHandler):

    def get(self, request_id):
        return self.output({'request_id': request_id})

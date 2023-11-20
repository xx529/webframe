from app.appserver import ServiceHandler, server, log
from app.appserver.config import LogConf
import pandas as pd


class AllUrls(ServiceHandler):
    URL = '/system/urls'

    def get(self):
        log.info('start server')
        rules = server.app.url_map.iter_rules()
        df_urls = pd.DataFrame([{'url': rule.rule, 'methods': ', '.join(sorted(rule.methods))} for rule in rules])
        df_urls.sort_values('url', inplace=True)
        data = df_urls.to_dict(orient='records')
        return self.output(data, code=200)


class ServerLog(ServiceHandler):
    URL = '/system/log'

    def get(self):
        with open(LogConf.SERVER_FILE, 'r') as f:
            lines = [eval(x) for x in f.readlines()]

        df_log = pd.DataFrame(lines)
        return self.output(df_log.to_dict(orient='records'))


class RuntimeLog(ServiceHandler):
    URL = '/system/log/<request_id>'

    def get(self, request_id):
        return self.output({'request_id': request_id})

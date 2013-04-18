# -*- coding: utf-8 -*-
import os
import sys

import bottle
from bottle import default_app, route, error
from language_middleware import LanguageMiddleware

from plants_libs.configparser import config_parser_dict
from plants_web.configs import LANGUAGES
from plants_web.configs.routes import ROUTES
from plants_web.libs.postgresplugin import PostgresPlugin
# from episte_web.libs import get_production_value
# from episte_web.libs.error_handler import ErrorHandler
# from episte_web.libs.mongo_middleware import MongoDBPlugin
# from episte_web.libs.bottle_plugins.solr import SolrPlugin
# from episte_web.libs.bottle_plugins.exceptions_handler import ExceptionsHandlerPlugin
# from episte_web.controllers import general


class StripPathMiddleware(object):
    def __init__(self, app, production):
        self.app = app
        self.production = production
    def __call__(self, env, start_response):
        env['PATH_INFO'] = env['PATH_INFO'].rstrip('/')
        # env['PLANTS_PRODUCTION'] = get_production_value(self.production)  
        env['PLANTS_PRODUCTION'] = False
        return self.app(env, start_response)

# def not_found(html):
#     return general.not_found()

# def not_allowed(html):
#     return general.not_allowed()


# Get config file path
if os.environ.get('PLANTS_WEB_CONFIG'):
    config_path = os.environ.get('PLANTS_CONFIG')
elif len(sys.argv) > 1:
    config_path = sys.argv[1]
else:
    config_path = os.path.join('/home/ubuntu/Plants-Web/scripts/local.cfg')

#Reading config file
config_dict = config_parser_dict(config_path)

postgres_config = config_dict.get('postgres', {'host':'localhost', 'port': 5432, 'dbname': 'leaves', 'user': 'postgres', 'password': 'postgres'})
# mongodb_config = config_dict.get('mongodb', {})
# web_config = config_dict.get('web', {})
# solr_config = config_dict.get('solr', {})
# email_config = config_dict.get('email', {})

# production = web_config.get('production') == 'True'
production = False
def process_routes(routes):
    for config in routes:
        route(config["url"], method=config["method"])(config["controller"])
    if production:
        error(404)(not_found)
        error(405)(not_allowed)
        # error(500)(handle_exception)


default_app.push()

# exception_handler = ExceptionsHandlerPlugin()
# bottle.install(exception_handler)

# solr = SolrPlugin(solr_config)
# bottle.install(solr)

process_routes(ROUTES)

application = default_app.pop()
application.catchall = False

if not production:
    bottle.debug(True)

# application = ErrorHandler(
application =  PostgresPlugin(
                LanguageMiddleware(
                        StripPathMiddleware(application, production),
                        default_language = 'en',
                        valid_languages = map(lambda x: x[0], LANGUAGES),
                        clean_url = True
                    # ),
                    ), 
                    **postgres_config
                )

             #    production = production,
             #    email_config = email_config
             # )

# if production:
#     import newrelic.agent
#     newrelic.agent.initialize('/home/production/configs/new_relic.ini', 'production')
#     application = newrelic.agent.wsgi_application()(application)
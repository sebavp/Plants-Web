# -*- coding: utf-8 -*-

from bottle import run, PasteServer

from serve_wsgi import *

def main():
    # reload = 'True' in web_config.get('reload', 'True')
    reload = True
    # web_port = int(web_config.get('port', '8080'))
    web_port = 8088
    run(app=application, host='0.0.0.0', port=web_port, server=PasteServer, reloader=reload)

if __name__ == "__main__":
    main()
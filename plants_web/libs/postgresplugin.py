# -*- coding: utf-8 -*-

from psycopg2 import connect, Error
from bottle import request

class PostgresPlugin(object):
	name = 'postgres'
	api = 2

	def __init__(self, app, **config_dict):
		self.app = app
		self.keyword = 'postgres'
		self.config_dict = config_dict

	def setup(self, app):
		''' Make sure that other installed plugins don't affect the same
			keyword argument.'''
		for other in app.plugins:
			if not isinstance(other, MongoDBPlugin): continue
			if other.keyword == self.keyword:
				raise Exception("Found another Postgres plugin with "\
				"conflicting settings (non-unique keyword).")

	def __call__(self, environ, start_response):
		# try:
		request.dbconnection = connect("host='%(host)s' port=%(port)s dbname='%(dbname)s' user='%(user)s' password='%(password)s'" % self.config_dict)
		request.db = request.dbconnection.cursor()
		return_ = self.app(environ, start_response)
		request.dbconnection.commit()
		request.db.close()
		request.dbconnection.close()
		del request.db
		return return_
		# except Error as e:
		# 	start_response(
  #               '500 Internal Server Error', 
  #               [
  #                   ('Cache-control', 'no-cache'),
  #                   ('Content-Type', 'text/html')
  #               ]
  #           )
		# 	return 'DataBase error', e.
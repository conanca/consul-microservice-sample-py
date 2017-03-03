# coding=utf-8
import flask
from app import app

import config
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger()

@app.route('/foo', methods=['GET'])
def foo():
	resp = flask.Response(response='bar', status=200)
	logger.info('foo...')
	return resp


@app.route('/health', methods=['GET'])
def health():
	resp = flask.Response(response='{"status": "UP"}', status=200)
	logger.info('health check...')
	return resp

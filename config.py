import logging
import logging.config
import os
import yaml

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
	CSRF_ENABLED = True
	DEBUG = True
	TESTING = False
	SECRET_KEY = os.environ['SECRET_KEY']
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	with open('config.yaml', 'r') as f:
		conf = yaml.safe_load(f.read())
		print(logging.__file__)
		logging.config.dictConfig(conf)

	logger = logging.getLogger(__name__)

	logger.debug('This is a debug message')
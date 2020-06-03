import os
from dotenv import load_dotenv
import logging
import logging.config
import yaml


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


# Project environment variable. Set in .flaskenv
class Config(object):
    # Encryption secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Set DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    with open('config.yaml', 'r') as f:
        conf = yaml.safe_load(f.read())
        print(logging.__file__)
        logging.config.dictConfig(conf)

    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message')

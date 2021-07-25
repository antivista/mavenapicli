from configparser import ConfigParser
import logging


# Read config file
config = ConfigParser(allow_no_value=False)
config.read_file(open('config.ini'))
N_ROWS = config['Maven_API_params']['N_ROWS']
LOG_LEVEL = config['Logging']['LOG_LEVEL']

# Manage logs structure
FORMAT = '%(asctime)s %(pathname)s %(lineno)d %(levelname)-8s   : %(message)s'
DATEFORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=FORMAT, datefmt=DATEFORMAT, level=LOG_LEVEL)

logging.info('Config loaded.')

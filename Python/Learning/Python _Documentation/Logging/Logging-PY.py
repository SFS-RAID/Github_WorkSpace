import logging
import os
os.system('cls')

# Create a logger of name ExampleLogger
logger = logging.getLogger('ExampleLogger')
# Minimum level for logger (default)
logger.setLevel(logging.DEBUG)
# Create a file handler and set the min level to debug, w is write mode (append can be used as a)
fh = logging.FileHandler('logs.log', 'w')
fh.setLevel(logging.DEBUG)
# Create a StreamHandler for Output and set the min level to error
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)
# Set and Add the format to fh and sh
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(sh)
logger.addHandler(fh)

# Log Some Info
logger.debug('Everything is working Fine')
logger.info('It is Recommended to do This')
logger.warning('Dont do this')
logger.error('There was an error')
logger.critical('The Code has Failed')

# setuplogging.py
# Import in all required scripts to get consistent logger behaviour

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('fdmulti')
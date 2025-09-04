#!/usr/bin/env python

# File Version: 2025-Sep-04: First version
#
# Author: matscorse
#
# Import in all required scripts to get consistent logger behaviour

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('fdmulti')
#!/usr/bin/env python

# File Version: 2025-Sep-04: First version
#
# Author: matscorse

from fdmulti.setuplogging import logger

class CHECK:

    """
    Check and resolve the validity of all pre-processing
    input arguments.
    """

    def __init__(self, args):
        
        self.rotation = args.rotation
        self.arrangement = args.WxH
        self.input = args.input
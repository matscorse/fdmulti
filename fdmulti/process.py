#!/usr/bin/env python

# File Version: 2025-Sep-04: First version
#
# Author: matscorse

from fdmulti.setuplogging import logger
from pathlib import Path
from PIL import Image

class PROCESS:

    """
    Processes the supplied image(s).
    """

    def __init__(self, args):
        
        self.rotation = args.rotation
        self.arrangement = eval(args.WxH.replace('x', ',').replace('X', ','))
        self.input = args.input
    

    def clip(self):
        with Image.open(self.input[0]) as im:
            this_path = Path(self.input[0])
            logger.info(f"Original Image  : {im.size}, {this_path.name}, {im.format}, {im.mode}")
            logger.info(f"Clip Arrangement: {self.arrangement}")
            clip_dims = (int(im.size[0]/self.arrangement[0]),
                            int(im.size[1]/self.arrangement[1]))
            logger.info(f"Clip Dimensions : {clip_dims}")

        return None
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
        for infile in self.input:
            with Image.open(infile) as im:
                this_path = Path(infile).absolute()
                this_dir = this_path.parent
                logger.info(f" Output Directory: {this_dir}")
                logger.info(f" Original Image  : {im.size}, {this_path.name}, {im.format}, {im.mode}")
                logger.info(f" Clip Arrangement: {self.arrangement}")
                clip_dims = (int(im.size[0]/self.arrangement[0]),
                                int(im.size[1]/self.arrangement[1]))
                logger.info(f" Clip Dimensions : {clip_dims}")

                framecount = 0
                for y_index in range(self.arrangement[1]):
                    for x_index in range(self.arrangement[0]):
                        clip_filename = this_path.stem + f"_{framecount}" + this_path.suffix
                        logger.info(f" Clipping and creating: {clip_filename}")
                        cropped = im.crop((x_index * clip_dims[0],
                                        y_index * clip_dims[1],
                                        (x_index * clip_dims[0])+clip_dims[0],
                                        (y_index * clip_dims[1])+clip_dims[1]))
                        if self.rotation != 0:
                            cropped = cropped.rotate(float(self.rotation), expand=True)
                        cropped.save(Path.joinpath(this_dir, clip_filename), quality=100)
                        framecount += 1


        return None
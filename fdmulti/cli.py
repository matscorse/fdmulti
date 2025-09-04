#!/usr/bin/env python

# File Version: 2025-Sep-04: First version
#
# Author: matscorse

import argparse
import sys
from fdmulti import __version__
from fdmulti.check import CHECK
from fdmulti.process import PROCESS


__DESCRIPTION__ = "Tool for processing and manupulating photographic images taken with the 'multi' burst record mode of the Sony Mavica Floppy Disk (FD) range of cameras"



def main():
    """
    cli entry point
    """
    
    parser = argparse.ArgumentParser(description=__DESCRIPTION__)

    parser.add_argument('-v', '--version', help="show this package version and exit",
                        action='version', version=__version__)
    parser.add_argument('-r', '--rotation', help="rotate the output (degrees)",
                        action="store", dest='rotation', default=0)
    parser.add_argument('-a', '--arrangement', help="clip arrangement in WxH, (default 3x3)",
                        action="store", dest='WxH', default='3x3')
    parser.add_argument('input', nargs='+', help="one or more input filename paths or directory paths")

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Now kick off main

    checked = CHECK(args)
    checked = checked.get_arguments()

    data = PROCESS(args)
    data.clip()



if __name__ == "__main__":
    main()
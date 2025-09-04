#!/usr/bin/env python

# File Version: 2025-Sep-04: First version
#
# Author: matscorse

import argparse
import sys
from fdmulti import __version__


__DESCRIPTION__ = "Tool for processing and manupulating photographic images taken with the 'multi' burst record mode of the Sony Mavica Floppy Disk (FD) range of cameras"



def main():
    """
    cli entry point
    """
    
    parser = argparse.ArgumentParser(description=__DESCRIPTION__)

    parser.add_argument('-v', '--version', help="show this package version and exit",
                        action='version', version=__version__)

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()


    # Now kick off main



if __name__ == "__main__":
    main()
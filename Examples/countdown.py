#!/usr/bin/env python
####################################################################################################
#
# Template based on recommendations from Matt Harrison in Beginning Python Programming
#
'''Creating example function to contribute to GitHub repo
'''

# Future Imports - Must be first, provides Python 2/3 interop
from __future__ import print_function       # print(<strings...>, file=sys.stdout, end='\n')
from __future__ import division             # 3/2 == 1.5, 3//2 == 1
from __future__ import absolute_import      # prevent implicit relative imports in v2.x
from __future__ import unicode_literals     # all string literals treated as unicode strings

# Imports
import argparse
import sys
import time

# Globals
# Note:  Consider using function/class/method default parameters instead of global constants where
# it makes sense
#BASE_FILE = 'file1'

# Metadata
__author__ = 'James R. Small'
__contact__ = 'james<dot>r<dot>small<at>outlook<dot>com'
__date__ = 'July 30, 2016'
__version__ = '0.0.1'


####################################################################################################
def countdown(start):
    '''Countdown from start.'''
    # Check Python version
    if sys.version_info > (3,0):
        USE_NEW_PRT = True
    else:
        USE_NEW_PRT = False
    while start > 0:
        print('{} '.format(start), end='\r')
        start -= 1
        time.sleep(0.250)
    start = 79
    while start > 0:
        if USE_NEW_PRT:
            print('\b-*', end='', flush=True)
        else:
            print('\b-*', end='')
            sys.stdout.flush()
        start -= 1
        time.sleep(0.005)
    start = 79
    while start > 0:
        if USE_NEW_PRT:
            print('\b\b-* \b\b', end='', flush=True)
        else:
            print('\b\b-* \b\b', end='')
            sys.stdout.flush()
        start -= 1
        time.sleep(0.005)
    print('\b\b* \b')

####################################################################################################
def main(args):
    '''Process arguments and call countdown'''
    parser = argparse.ArgumentParser(description='Simple example program using a function')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-s', '--start', help='number to start countdown from', default=10,
                        type=int, metavar='STARTING_NUMBER')
    parser.add_argument('-v', '--verbose', action='store_true', help='display verbose output',
                        default=False)
    args = parser.parse_args()

    if args.verbose:
        print('Start = {}, type = {}'.format(args.start, type(args.start)))
    countdown(args.start)

# Call main and put all logic there per best practices.
# No triple quotes here because not a function!
if __name__ == '__main__':
    # Recommended by Matt Harrison in Beginning Python Programming
    # sys.exit(main(sys.argv[1:]) or 0)
    # Simplied version recommended by Kirk Byers
    main(sys.argv[1:])


####################################################################################################
# Post coding
#
# pylint <script>.py
#   Score should be >= 8.0
#
# Future:
# * Testing - doctest/unittest/other
# * Logging
#


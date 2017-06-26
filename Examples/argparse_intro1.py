# Reference:  https://docs.python.org/2/library/argparse.html

# Imports
import argparse

# Main
#parser = argparse.ArgumentParser()
#
# Add description of program
parser = argparse.ArgumentParser(description="calculate x to the power of y")
#
# Basics - gives you -h|--help for free
#parser.parse_args()
#
# Positional argument
# - defaults to type string
#parser.add_argument('square',help='display a square of a given number')
# - change to type int
#parser.add_argument('square',help='display a square of a given number',type=int)
#args = parser.parse_args()
#print args.square**2
#
# Optional argument
# - expects integer after verbosity, e.g. 1 or 2 or 5
#parser.add_argument("--verbosity",help="increase output verbosity")
# - do this way if just want to be able to toggle an option on
#parser.add_argument("--verbose",help="increase output verbosity",action="store_true")
# - include 'short' flag (-v|--verbose)
#parser.add_argument("-v","--verbose",help="increase output verbosity",action="store_true")
#args = parser.parse_args()
#if args.verbose:
#    print "verbosity turned on"
#
# Combine positional and optional arguments
#parser.add_argument('square',help='display a square of a given number',type=int)
# - limit verbosity choices to one of 0|1|2
#parser.add_argument("-v","--verbosity",help="increase output verbosity",type=int,choices=[0,1,2])
# - now verbosity flag done with either -v|-vv
#parser.add_argument("-v","--verbosity",help="increase output verbosity",action="count",default=0)
#args = parser.parse_args()
#answer = args.square**2
#if args.verbosity >= 2:
#    print "the square of {} equals {}".format(args.square,answer)
#elif args.verbosity >= 1:
#    print "{}^2 == {}".format(args.square,answer)
#else:
#    print answer
#
# Use mutually exclusive arguments
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print answer
elif args.verbose:
    print "{} to the power {} equals {}".format(args.x, args.y, answer)
else:
    print "{}^{} == {}".format(args.x, args.y, answer)


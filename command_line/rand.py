
import argparse
from random import randint

# define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('count', action = 'store', type = int, help = 'Count of random integers to be generated')

# Add optional arguments
parser.add_argument('-r', '--range', metavar = ('lower', 'upper'), nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')

parser.add_argument('-c', '--const', action = 'store_const', const = 10, default = 0, help = 'generate 10 additional random numbers (in addition to Count)')

parser.add_argument('-m', '--multiply', action = 'count', help = 'multiply the number of random numbers by the number of times this flag appears')

parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Verbose mode')

# parse command line arguments
args = parser.parse_args()

# program

# if args.const is used, add 10 to the count entered by the user
num_of_rands = (args.count + args.const)

# when args.multiply is not used, its value is None
if (args.multiply != None):
    num_of_rands = num_of_rands * args.multiply

if args.verbose:
    print("Generating {:d} random integer in the range [{:d}, {:d}]".format(num_of_rands, args.range[0], args.range[1]))
            
for i in range(num_of_rands):
    print(randint(args.range[0], args.range[1]))
#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Process some integers.")

# positional argument
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='a sequence of integers for the program to process'
                    )

# optional flag
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help="sum the integers (default: find the maximum)"
                    )

args = parser.parse_args()

print(args)

# Call max or sum (if --sum was specified)
print(args.accumulate(args.integers))

args = parser.parse_args('1 4 7 2'.split())

print(args)

print(args.accumulate(args.integers))


#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Process some integers.")

# positional argument
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='a sequence of integers for the program to process'
                    )

args = parser.parse_args()

print(args.integers)

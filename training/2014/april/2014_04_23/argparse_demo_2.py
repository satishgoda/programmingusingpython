#!/usr/bin/env python

import sys
from pprint import pprint
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Demo for argparse")
    
    parser.add_argument('--debug', '-d', 
                        action='store_true',
                        help='nothing much here'
                        )

    parser.add_argument('integers', type=int,
                        nargs=2, 
                        action='store',
                        help='data for the program to process'
                        )

    args = parser.parse_args()

    pprint(args)

    if args.debug:
        print("Enabling debug mode")
    else:
        for arg in args.integers:
            print(arg)


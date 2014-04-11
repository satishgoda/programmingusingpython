#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Generate classtree for a class using its C3 MRO")


# positional argument
parser.add_argument('booleans', metavar='bool', type=bool, nargs=2, default=False,
                    help='Boolean flags to control classtree output'
                    )


args = parser.parse_args()

print(args)




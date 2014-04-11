import argparse

parser = argparse.ArgumentParser(description="Class Tree using inspect module")

parser.add_argument('--default', '-d', action='store_true')
parser.add_argument('--qualname', '-q', action='store_true')

args = parser.parse_args()

print(args)

# script to clean the data files
import argparse
import preprocessor as p
import sys


parser = argparse.ArgumentParser(description='This script will clean the data')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

args = parser.parse_args()

f = open(args.input)

for line in f:
	print(p.clean(line))

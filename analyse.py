import argparse
import sys


parser = argparse.ArgumentParser(description='This script will clean the data')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

args = parser.parse_args()

f = open(args.input)
h = {}
l = 0
for line in f:
	for c in line:
		l += 1
		if c in h:
			h[c] += 1
		else:
			h[c] = 1

for i in sorted(h, key=h.get):
	print(i,h[i]/l*100)
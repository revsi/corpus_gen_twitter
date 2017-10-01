# script to clean the data files
import argparse
import sys
import re
parser = argparse.ArgumentParser(description='This script will clean the data')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

args = parser.parse_args()

f = open(args.input)

for line in f:
	cur_line = ''
	for i in line:
		if i != ' ':
			c_num = ord(i)
			if 2000<c_num<3500 or 32<c_num<65:
				cur_line = ''.join([cur_line, i])
		else:
			cur_line = ''.join([cur_line, i])
	cur_line = re.sub(r"[\.]+", ".", cur_line)
	cur_line = re.sub(r"[\ ]+", " ", cur_line)
	cur_line = re.sub(r"[!]+", "!", cur_line)
	cur_line = re.sub(r"[\?]+", "?", cur_line)

	print(cur_line)

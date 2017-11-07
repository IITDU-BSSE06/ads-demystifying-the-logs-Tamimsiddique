#!/usr/bin/python


import sys

for line in sys.stdin:
	count = line.strip().split(" - - ")
	if len(count) == 2:
		ip, rest = count
		print "{0}\t{1}".format(ip, rest)

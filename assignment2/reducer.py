#!/usr/bin/python

import sys

countTotal = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	ip, rest = data_mapped
	if '/assets/js/the-associates.js' in rest:
		countTotal=countTotal+1

print str(countTotal)

#!/usr/bin/python
import urlparse

import sys

for line in sys.stdin:
	count = line.strip().split(" ")
	if len(count) == 10:
		x0, x1 ,x2 ,x3 ,x4 ,x5 ,x6 ,x7 ,x8 ,x9= count
		path = urlparse.urlparse(x6).path

		print "{0}\t{1}".format(x6,x6)

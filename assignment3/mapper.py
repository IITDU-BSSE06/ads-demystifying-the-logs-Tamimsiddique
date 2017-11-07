#!/usr/bin/python
import urlparse

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		x0, x1 ,x2 ,x3 ,x4 ,x5 ,x6 ,x7 ,x8 ,x9= data
#		path = urlparse.urlparse(x6).path

		print "{0}\t{1}".format(x6,x6)

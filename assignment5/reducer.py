#!/usr/bin/python

import sys

uniqueFiles=0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, fullPath = data_mapped

    if oldKey and oldKey != thisKey:
        uniqueFiles+=1
        oldKey = thisKey;
        salesTotal = 0
    oldKey = thisKey

print str(uniqueFiles)

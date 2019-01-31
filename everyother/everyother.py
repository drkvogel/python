#!/usr/bin/env python3

# copy input file to output file but delete every other line
# for e.g. text copied from gmail

import sys

if len(sys.argv) < 3:
    print("usage: %s <input filename> <output filename>" % sys.argv[0])
    exit(0)

infilename = sys.argv[1]
outfilename = sys.argv[2]
infile = open(infilename, "r")
outfile = open(outfilename, "w")
count = 0

for line in infile:
    # print('count: %s' % count)
    if count % 2 == 0:
        outfile.write(line)
        # print('write')
    else:
        pass
        # print('skip')
    count = count + 1

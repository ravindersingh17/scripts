#!/usr/bin/env python3
import sys

lines = open(sys.argv[1]).readlines()
try: lines[int(sys.argv[2])- 1] = "#" + lines[int(sys.argv[2])]
except IndexError: pass
with open(sys.argv[1],"w") as f:
    for l in lines:
        f.write(l)

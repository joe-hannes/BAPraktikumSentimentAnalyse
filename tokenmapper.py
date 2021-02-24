#!/usr/bin/env python
import re
import sys
import json

for line in sys.stdin:
    x = json.loads(line)
    try:
        y = x['text']

        y = line.strip()
        tokens = y.split()
        for token in tokens:
            print("%s\t%s" % (token, 1))
    except KeyError:
        pass

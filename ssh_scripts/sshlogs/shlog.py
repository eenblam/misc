#!/usr/bin/env python

import fileinput
import sys
from itertools import tee

d = {
        # This line should be immediately followed by
        # "...input_userauth_request: invalid user someuser..."
        ": Invalid user": "invalid",
        " - POSSIBLE BREAK-IN ATTEMPT!": "proxy",
        ": Accepted": "accepted"
    }

def classifier_factory(d):
    #TODO This doesn't account for multiple matches on a single line
    def classify(line):
        for k,v in d.items():
            if k in line:
                return(line, v)
        return(line, None)
    return classify

def split_logs(lines, key):
    # Params:
    # - lines: A source of strings, presumably a log file
    # - key: A dictionary of the form "match string":"label"
    #
    # Returns a list of the form [(key, filtered logs)]
    # ...where filtered logs is a filtered generator fed from lines parameter

    classify = classifier_factory(key)
    values = set(key.values())

    lines = (classify(line) for line in lines)
    pipes = zip(values, tee(lines, n=len(values)))
    pipes = [(key, (line for line,flag in pipe if flag is key))
            for key,pipe in pipes if key is not None]

    return sorted(pipes, key = lambda pair: pair[0])



with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
    lines = (line.strip() for line in lines)
    pipes = split_logs(lines, key=d)
    pipes = dict(pipes)

    for key, pipe in pipes.items():
        print(key + "\n")
        for x in pipes:
            print("\t" + x)

# Note that the code below only catches data
# and writes each record to the appropriate file.
# There's no in-flight modification. It's a very simple split.
#TODO load dict
#TODO open a buffer for each output file
with fileinput.input(sys.argv[2:]) as lines:
    lines = (line.strip() for line in lines)
    for line in lines:
        for k,v in d.items():
            if k in line:
                #write to file v
            

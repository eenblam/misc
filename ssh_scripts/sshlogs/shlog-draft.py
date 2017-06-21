#!/usr/bin/env python

import sys
#import os
#import regex
from itertools import tee

d = {
        # This line should be immediately followed by
        # "...input_userauth_request: invalid user someuser..."
        ": Invalid user": "invalid",
        " - POSSIBLE BREAK-IN ATTEMPT!": "proxy",
        ": Accepted": "accepted"
    }

def classify(line, d):
    for k,v in d.items():
        if k in line:
            return(line, v)
    return(line, None)

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
    lines = (line.strip() for line in lines)
    lines = (classify(line, d) for line in lines)

    values = set(d.values())
    pipes = zip(values, tee(lines, n=len(values)))

    pipes = ((key, (line for line, flag in pipe if flag is key))
            for key, pipe in pipes if key is not None)
            #TODO add flag for dropping non-matches
            # for key, pipe in pipes if key is not None or keep_mismatches)

    # I'd say the above is a lot nicer than this:
    #   def filterify(pipes):
    #       for key, pipe in pipes:
    #           def outgen():
    #               for line, flag in pipe:
    #                   if flag is key:
    #                       yield line
    #           yield (key, outgen())
    #
    #    pipes = filterify(pipes)

    pipes = sorted(pipes, key = lambda pair: pair[0])
    for key, pipe in pipes:
        print(key + "\n")
        for x in pipes:
            print("\t" + x)

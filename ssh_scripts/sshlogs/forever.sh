#!/bin/bash
stdbuf -o0 python out.py | python in.py -

# Depending on your system, you may instead need this:
#unbuffer ./in.py | ./out.py

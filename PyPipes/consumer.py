#!/usr/bin/env python
import fileinput
import sys

# Reverse each incoming line
input_lines = fileinput.input(sys.argv[2:])
for line in input_lines:
    line = line.strip()[::-1] + '\n'
    sys.stdout.write(line)

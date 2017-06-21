#!/bin/bash
stdbuf -o0 python factory.py | python consumer.py -

# Depending on your system, you may instead need this:
#unbuffer python factory.py | python consumer.py -

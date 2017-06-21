#!/usr/bin/env python

from sys import stdout
from time import sleep

i = 0
while(True):
    stdout.write(str(i) + '\n')
    i += 1
    sleep(1)

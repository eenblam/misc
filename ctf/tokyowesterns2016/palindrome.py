#!/usr/bin/env python

# https://score.ctf.westerns.tokyo/problems/4

from pwn import *
from itertools import permutations

def check_palindrome(s):
    length = len(s)
    half = length / 2
    return s[:half] == s[-half:][::-1]

def get_palindrome(inp):
    perms = permutations(inp)
    perms = ((p, ''.join(p)) for p in perms)
    for p in perms:
        if check_palindrome(p[1]):
            return ' '.join(p[0])
    return False

r = remote('ppc1.chal.ctf.westerns.tokyo', 31111)
r.recvuntil("Let's play!")
r.recvlines(2)
while True:
    line = r.recvline()
    print line
    try:
        left, right = line.split(':')
    except ValueError:
        # Case: Ben's an idiot
        print "Bad line..."
        continue
    if left == 'Case':
        continue
    if left == 'Input':
        right = right.strip().split()
        # skip count
        answer = get_palindrome(right[1:])
        if not answer:
            print 'No palindrome found for:\t{}'.format(right[1:])
            break # Failed
        r.sendlineafter('Answer: ', answer)
    # else Judge (or Answer if bug)

r.close()

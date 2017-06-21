#!/usr/bin/env python

# https://score.ctf.westerns.tokyo/problems/6

import math
from Crypto.Util.number import *
import Crypto.PublicKey.RSA as RSA

with open('key1','r') as f1, open('key2', 'r') as f2:
    # Short n
    n1 = long(f1.readline().strip())
    # Long n
    n2 = long(f2.readline().strip())
    #e = long(f2.readline().strip())
    e = long(65537)

rhs = ((n2 - n1 - 4) / 2) + 1
f1 = n1 - rhs
f2 = n1 + rhs

d1 = inverse(e, f1)
d2 = inverse(e, f2)
rsa1 = RSA.construct((n1, e, d1))
rsa2 = RSA.construct((n2, e, d2))

with open('encrypted', 'r') as f, open('out', 'w') as out:
    encrypted = long(f.read().strip())
    msg = rsa1.decrypt(rsa2.decrypt(encrypted))
    out.write(long_to_bytes(msg))

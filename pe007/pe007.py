# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 2018

@author: NieXiaoming

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from functools import reduce
import math
def isprime(n):
    return not reduce(lambda x,y:x or y,[n%x==0 for x in range(2,math.ceil(math.sqrt(n))+1)])

def primes():
    x=2
    yield x
    while True:
        x=x+1
        if isprime(x):
            yield x

N=10001
n=1
for x in primes():
    print('%s -- %s'%(n,x))
    if n==N:
        break
    else:
        n=n+1

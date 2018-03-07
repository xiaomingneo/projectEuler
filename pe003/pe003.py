# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 2018

@author: NieXiaoming

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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
        
print(isprime(10086647))
N = 600851475143
for a in primes():
    while N%a==0:
        N=N//a
    if isprime(N):
        print('==========')
        print(N)
        print(isprime(10086647))
        break
    print('%s-->%s'%(a,N))

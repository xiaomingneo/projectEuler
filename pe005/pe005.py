# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 2018

@author: NieXiaoming

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

from functools import reduce
import math


def isprime(n):
    if n==2 or n==3:
        return True
    else:
        print(n)
        return not reduce(lambda x,y:x or y,[n%x==0 for x in range(2,math.ceil(math.sqrt(n))+1)])

def primes():
    x=2
    yield x
    while True:
        x=x+1
        if isprime(x):
            yield x

def fact(n):
    ps=dict()
    for x in primes():
        if n==1 or isprime(n):
            ps[n]=1
            return ps
        while n%x==0:
            n=n//x
            if x in ps:
                ps[x]=ps[x]+1
            else:
                ps[x]=1

ps1=dict()
for x in range(2,20):
    ps=fact(x)
    for item in ps:
        if item in ps1:
            if ps[item]>ps1[item]:
                ps1[item]=ps[item]
        else:
            ps1[item]=ps[item]

print('=====')
print(reduce(lambda x,y:x*y,[key**ps1[key] for key in ps1]))

        

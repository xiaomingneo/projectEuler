# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 2018

@author: NieXiaoming
"""

def fib(max):
    n,a,b=0,1,1
    while b<max:
        a,b=b,a+b
        yield a
print(sum([x for x in fib(4000000) if x%2==0]))

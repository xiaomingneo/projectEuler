# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 2018

@author: NieXiaoming

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""


def diff_sqsu_susq(n):
    return n*(n+1)*(n-1)*(3*n+2)/12

print(diff_sqsu_susq(10))
print(diff_sqsu_susq(100))

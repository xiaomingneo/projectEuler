# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 2018

@author: NieXiaoming

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindromic(x):
    sx=str(x)
    if sx==sx[::-1]:
        return True
    else:
        return False
palinNumbers = [x for x in range(1000000,10000,-1) if isPalindromic(x)]
findIt=False
for x in palinNumbers:
    for y in range(999,100,-1):
        if x%y==0 and x/y>100 and x/y<1000:
            print('%s = %s * %s'%(x,y,x//y))
            findIt=True
            break
    if findIt:
        break
        

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import timeit
temps1=-1
temps2=-1
temps3=-1

def est_premier_1(n):
    d = 2
    while n%d != 0:
        d = d+1
    if n == d : return True
    else :      return False

def est_premier_2(n):
    d = 2
    while(d**2 <= n):
        if(n%d == 0):
            return False
        d = d+1
    return True

def est_premier_3(n):
    d = 2
    if(n%d == 0):
            return False
    d = d+1
    while(d**2 <= n):
        if(n%d == 0):
            return False
        d = d+2
    return True

def benchmark():
    temps1 = timeit.timeit("est_premier_1(101)",setup="from Corr import est_premier_1",number=100000)
    temps2 = timeit.timeit("est_premier_2(101)",setup="from Corr import est_premier_2",number=100000)
    temps3 = timeit.timeit("est_premier_3(101)",setup="from Corr import est_premier_3",number=100000)
    return temps1,temps2,temps3


    
def fonction():
    
    return benchmark()
#!/usr/bin/python3
# -*- coding: utf-8 -*-


def minuscule(a):
    b = ord(a)
    if ( 64 < b and b < 91 ):
        c = b + 32
        return chr(c) 
    return a

def majuscule(a):
    b = ord(a)
    if ( 96 < b and b < 123 ):
        c = b - 32
        return chr(c) 
    return a

def switch(c):
    a = majuscule(c)
    if(a == c):
        return minuscule(c)
    return a

def majLock(t):
    result = ""
    for c in t:
        result = result + switch(c)
    return result
    

def fonction(a):
    return majLock(a)
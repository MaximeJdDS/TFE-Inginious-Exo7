#!/usr/bin/python3
# -*- coding: utf-8 -*-


def minuscule(a):
    b = ord(a)
    if ( 64 < b and b < 91 ):
        c = b + 32
        return chr(c) 
    return a

def fonction(a):
    return minuscule(a)
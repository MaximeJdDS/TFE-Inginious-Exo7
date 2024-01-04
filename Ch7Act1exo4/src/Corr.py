#!/usr/bin/python3
# -*- coding: utf-8 -*-


def pythagore(data):
    result = []
    for i in data:
        if (i[2]**2) == (i[1]**2) + (i[0]**2) :
            result = result + [True]
        else :
            result = result + [False]
    
    return result

def fonction(data):
    return pythagore(data)
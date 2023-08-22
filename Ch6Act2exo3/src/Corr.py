#!/usr/bin/python3
# -*- coding: utf-8 -*-


def verlan(mot):
    i=len(mot)-1
    result=""
    while(i>=0):
        result = result +mot[i]
        i = i-1
    return result

def fonction(s):
    return verlan(s)
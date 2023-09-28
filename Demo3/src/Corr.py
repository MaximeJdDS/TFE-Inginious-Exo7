#!/usr/bin/python3
# -*- coding: utf-8 -*-


def facto(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

def fonction(n):
    return facto(n)
#!/usr/bin/python3
# -*- coding: utf-8 -*-


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
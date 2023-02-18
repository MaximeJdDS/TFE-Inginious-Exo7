#!/usr/bin/python3
# -*- coding: utf-8 -*-


def est_premier_2(n):
    d = 2
    while(d**2 <= n):
        if(n%d == 0):
            return False
        d = d+1
    return True
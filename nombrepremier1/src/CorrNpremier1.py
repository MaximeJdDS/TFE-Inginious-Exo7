#!/usr/bin/python3
# -*- coding: utf-8 -*-


def est_premier_1(n):
    d = 2
    while n%d != 0:
        d = d+1
    if n == d : return True
    else :      return False
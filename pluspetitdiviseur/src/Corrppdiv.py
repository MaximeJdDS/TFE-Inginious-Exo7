#!/usr/bin/python3
# -*- coding: utf-8 -*-


def plus_petit_diviseur(n):
    d=2
    while n%d !=0 :
        d = d+1
    return d
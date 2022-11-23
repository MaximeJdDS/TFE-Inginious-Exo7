#!/usr/bin/python3
# -*- coding: utf-8 -*-


def quotient_reste(a, b):
    print(a,b)
    q=a//b
    r=a%b
    print(a//b)
    print(a%b)
    print(0<= r < b)
    print(a == b*q +r)

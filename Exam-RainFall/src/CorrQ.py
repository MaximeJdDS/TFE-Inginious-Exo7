#!/usr/bin/python3
# -*- coding: utf-8 -*-


def rainfall(l):
    sum = 0
    count = 0
    if l[0]==9999:
        return 0.0
    for i in l:
        if i == 9999:
            break
        if i<0 :
            i = 0
        sum = sum + i
        count = count + 1
    return sum/count    
                      

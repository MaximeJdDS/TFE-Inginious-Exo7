#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fonction():
    sac = []
    for c in range(10):
        for d in range(10):
            for u in range(10):
                n = 100*c + 10*d + u
                if (u==3):
                    if(c+d+u >= 15):
                        if(d%2==0):
                            sac.append(n)
    return sac
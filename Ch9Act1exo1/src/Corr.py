#!/usr/bin/python3
# -*- coding: utf-8 -*-


def ecritXfois(a,b,c):
    
    fic = open(a,"w")
    while(c>0):
        fic.write(b)
        c = c - 1
    fic.close()

def fonction(a,b,c):
    return ecritXfois(a,b,c)
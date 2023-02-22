#!/usr/bin/python3
# -*- coding: utf-8 -*-


def est_premier(n):
    d = 2
    if(n%d == 0):
            return False
    d = d+1
    while(d**2 <= n):
        if(n%d == 0):
            return False
        d = d+2
    return True

def nombres_jumeaux_apres(n):
    if(n%2 == 0): #even
        i=n+1
    else :        #odd
        i=n+2
    found = False
    while(not(found)):
        if(est_premier(i) and est_premier(i+2)):
            found = True 
        else:
            i = i+2
    return i

def fonction(n):
    return nombres_jumeaux_apres(n)
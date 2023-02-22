#!/usr/bin/python3
# -*- coding: utf-8 -*-


def nombre_germain_apres(n):
    if(n%2 == 0): #even
        i=n+1
    else :        #odd
        i=n+2
    found = False
    while(not(found)):
        if(est_premier(i) and est_premier(2*i+1)):
            found = True 
        else:
            i = i+2
    return i

def fonction():
    return fonction()
#!/usr/bin/python3
# -*- coding: utf-8 -*-


def distance_hamming(mot1,mot2):
    if(len(mot1)!=len(mot2)): return -1
    i=0
    count=0
    while(i<len(mot1)):
        if(mot1[i]!=mot2[i]):
            count=count+1
        i=i+1    
    return count

def fonction(a,b):
    return distance_hamming(a,b)
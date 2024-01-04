#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fichierToList(a):
    
    fic = open(a,"r")
    result = []
    for ligne in fic:
        result = result + [int(ligne)]
    fic.close()
    return result

def fonction(a):
    return fichierToList(a)
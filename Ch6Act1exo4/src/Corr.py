#!/usr/bin/python3
# -*- coding: utf-8 -*-


def pluriel(mot):
    if(mot[len(mot)-1]=="s"):
        return mot
    if(mot[len(mot)-2:len(mot)]=="al"):
        return mot[0:len(mot)-2] + "aux"
    else:
        return mot +"s"

def fonction(s):
    return pluriel(s)
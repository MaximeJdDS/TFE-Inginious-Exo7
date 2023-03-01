#!/usr/bin/python3
# -*- coding: utf-8 -*-


def pluriel(mot):
    if(mot[len(mot)-1]!="s"):
        return mot+"s"
    else:
        return mot


def fonction(s):
    return pluriel(s)
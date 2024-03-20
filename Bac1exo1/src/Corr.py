#!/usr/bin/python3
# -*- coding: utf-8 -*-


def filtreTableau(a,b):
    tab =[]
    for e in a:
        if not e in b:
            tab.append(e)
    return tab

def fonction(a,b):
    return filtreTableau(a,b)
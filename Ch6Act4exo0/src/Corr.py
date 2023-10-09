#!/usr/bin/python3
# -*- coding: utf-8 -*-


def shift(lettre):
    lettre = ord(lettre) - 32
    lettre = chr(lettre)
    return lettre

def fonction(x):
    return shift(x)
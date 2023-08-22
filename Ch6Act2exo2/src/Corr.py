#!/usr/bin/python3
# -*- coding: utf-8 -*-


def latin_cochon(s):
    voyelles = ["a","i","e","u","y","o"]
    if(s[0] not in voyelles):
        return s[1:len(s)]+s[0]+"um"
    else:
        return s

def fonction(s):
    return latin_cochon(s)
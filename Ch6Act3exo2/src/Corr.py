#!/usr/bin/python3
# -*- coding: utf-8 -*-


def position_de_AT(adn):
    i = 0
    while (i<len(adn)-1):
        if(adn[i]=="A"):
            if(adn[i+1]=="T"):
                return i
        i=i+1
    return None

def fonction(s):
    return position_de_AT(s)
#!/usr/bin/python3
# -*- coding: utf-8 -*-


def presence_de_A(adn):
    for i in adn:
        if i == "A":
            return True
    return False

def fonction(s):
    return presence_de_A(s)
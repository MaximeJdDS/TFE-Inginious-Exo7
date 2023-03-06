#!/usr/bin/python3
# -*- coding: utf-8 -*-


def est_un_palindrome(mot):
    i = 0
    while(i<len(mot)):
        if(mot[i]!=mot[len(mot)-i-1]):
            return False
        i = i +1
    return True

def fonction(s):
    return est_un_palindrome(s)
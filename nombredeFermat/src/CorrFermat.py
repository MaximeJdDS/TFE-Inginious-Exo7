#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def estpremier(n): 
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i) == 0:
                return False
        return True


def F(n):
    Fermat = 2**(2**n) + 1
    return Fermat
    
    
def contreExemple():
    return 4294967297
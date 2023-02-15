#!/usr/bin/python3
# -*- coding: utf-8 -*-




def F(n):
    Fermat = 2**(2*n) + 1
    return Fermat
    
    
def contreExemple():
	i = 1
	while(est_premier(F(n))):
		i = i+1
	return F(i)
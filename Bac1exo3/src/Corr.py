#!/usr/bin/python3
# -*- coding: utf-8 -*-



def f():
    return [0,1,2]    

def MatrixCheck(matrix):
    checklist = f()
    for ligne in matrix:
        for j in ligne:
            if j in checklist:
                checklist.remove(j)
                if len(checklist) == 0 :
                    return True
    return False   
            
    
def fonction(n):
	return MatrixCheck(n)
#!/usr/bin/python3
# -*- coding: utf-8 -*-



def MatrixReduc(matrix):
    length = len(matrix)
    i,j = 0,0
    n = int(length/2)
    result = [[0 for _ in range(n)] for _ in range(n)]
    while(i<n):
        while(j<n):
            moyenne = (matrix[2*i][2*j] + matrix[2*i+1][2*j] + matrix[2*i][2*j+1] + matrix[2*i+1][2*j+1])/4
            result[i][j] = moyenne 
            j = j + 1
    
        i = i + 1    
    return result  
            
    
def fonction(n):
	return MatrixReduc(n)
#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Chien:
    def __init__(self,nom,race,x,y):
        self.nom  = nom
        self.race = race
        self.x    = x
        self.y    = y
        
    def wouaf():
        print("Wouaf!")
     
    def viensIci(self,x,y):
        self.x = x
        self.y = y




def fonction(nom,race,x,y):
    return Chien(nom,race,x,y)
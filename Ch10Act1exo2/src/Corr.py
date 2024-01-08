#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Bourse:
    def __init__(self,gold,silver,bronze):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        
    def __str__(self):
        return str(self.gold)+" piece(s) d'or, "+ str(self.silver)+" piece(s) d'argent et "+str(self.bronze)+" piece(s) de bronze."
        
    def __add__(self,other):
        W = Bourse(self.gold+other.gold,self.silver+ other.silver, self.bronze+ other.bronze)
        return W
        
    def echange(self):
        if(self.bronze//100 != 0 ):
            self.silver = self.silver + (self.bronze//100)
            self.bronze = self.bronze%100
        if(self.silver//100 != 0 ):
            self.gold = self.gold + (self.silver//100)
            self.silver = self.silver%100
            
    def __eq__(self,other):
        return ((self.gold == other.gold) and (self.silver == other.silver) and (self.bronze == other.bronze))




def fonction(x,y,z):
    return Bourse(x,y,z)
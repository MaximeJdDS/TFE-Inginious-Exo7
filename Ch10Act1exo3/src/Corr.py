#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Plat:
    def __init__(self,ingredient,prix,nom,isVege):
        self.ingredient = ingredient
        self.prix = prix
        self.nom = nom
        self.isVege = isVege
            
    def isVege(self):
        return self.isVege
            
        
    def service(): # pour servir automatiquement le plat
        return 0
            
class Pizza(Plat):
    def __init__(self,ingredient,prix,nom,isVege,typeDeFour):
        
        super().__init__(ingredient,prix,nom,isVege)
        self.typeDeFour = typeDeFour
        
    
        
    def surfacePizza(self,diametre):
        r = diametre/2
        return 3.14 * r**2
            
    def __eq__(self,other):
        return ((self.ingredient == other.ingredient) and (self.prix == other.prix) and (self.nom == other.nom) and (self.isVege == other.isVege) and (self.typeDeFour == other.typeDeFour))




def fonction(x,y,z,e,r):
    return Pizza(x,y,z,e,r)
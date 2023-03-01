#!/usr/bin/python3
# -*- coding: utf-8 -*-


def affiche_conjugaison(verbe):
    if(verbe[len(verbe)-2:len(verbe)]!="er"):
        print("Ce n'est pas un verbe du premier groupe.")
    else:
        pp = verbe[0:len(verbe)-2] #participe passer
        print("je "+pp+"e, tu "+pp+"es, il "+pp+"e, nous "+pp+"ons, vous "+pp+"ez, ils "+pp+"ent")

def fonction(s):
    affiche_conjugaison(s)
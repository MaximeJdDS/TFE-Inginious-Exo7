#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'latin_cochon')):
    tagDico = Misconceptions.runAllFunc(student.latin_cochon)
Misconceptions.tagTransfer(tagDico)

def compare(mot1, mot2):
    return mot1.lower() == mot2.lower()


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'latin_cochon'), _("Tu n\'as pas defini la bonne fonction. La fonction 'latin_cochon' est introuvable."))

    

    def test_result_normalCase(self):
        a = ["VITRE","BLANCHE","MotsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","test"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\"\nMalgrès ce que peut te montrer les valeurs de retour, ne perd pas de temps avec les Majuscules/minuscules. Concentre toi sur l'emplacement des lettres.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            if(compare(stu_ans,corr_ans)):#Bonne réponse 
                self.assertEqual(True, True, "Bonne réponse.")
            else:
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            
    def test_result_voyelleCase(self):
        a = ["etude","impossible","otsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","arbre","utile","yakari"]
        ansresult   = _("Le mot \"{}\" commence par une voyelle, par consequent, tu ne dois pas le \"cochon-latiner \".\n Ta fonction a renvoyé \"{}\". Pour rappel, voici la liste des voyelles : [\"a\",\"i\",\"e\",\"u\",\"y\",\"o\"]. \n N\'hésite pas à aller revoir la page 43 du syllabus exo7 pour tester si un caractère fait partie d'un tableau de caractère.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            if(compare(stu_ans,corr_ans)):#Bonne réponse 
                self.assertEqual(True, True, "Bonne réponse.")
            else:
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            
            


if __name__ == '__main__':
    unittest.main()

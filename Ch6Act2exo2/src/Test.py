#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'latin_cochon'), _("Tu n\'as pas defini la bonne fonction. La fonction 'latin_cochon' est introuvable."))

    

    def test_result_normalCase(self):
        a = ["vitre","blanche","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","test"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            
    def test_result_voyelleCase(self):
        a = ["etude","impossible","otsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","arbre","utile","yakari"]
        ansresult   = _("Le mot \"{}\" commence par une voyelle, par consequent, tu ne dois pas le \"cochon-latiner \".\n Ta fonction a renvoyé \"{}\". Pour rappel, voici la liste des voyelles : [\"a\",\"i\",\"e\",\"u\",\"y\",\"o\"]. \n N\'hésite pas à aller revoir la page 43 du syllabus exo7 pour tester si un caractère fait partie d'un tableau de caractère.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            
            


if __name__ == '__main__':
    unittest.main()

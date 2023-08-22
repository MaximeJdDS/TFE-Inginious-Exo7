#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'double'), _("Tu n\'as pas defini la bonne fonction. La fonction 'double' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(3, 169) for _ in range(10)]
        ansresult   = _("Pour la valeur n = {}, la réponse attendu est {} et ta fonction a renvoyé {}.")
        anssame = _("Pour la valeur n = {}, la réponse attendu est {} et ta fonction a renvoyé {}. \nN'oublie pas, l'instruction n = 2 permet de modifier la valeur qui est contenu dans \"n\" \npeu importe ce qu'il y avait avant. \nDans ce cas ci, on ne veut pas la valeur 2 mais le double, donc fois 2.")
        anstwo   = _("Pour la valeur n = {}, la réponse attendu est {} et ta fonction a renvoyé {}. \nIl semblerait que ta fonction renvoie systematiquement 2. \nCe n\'est pas ce qu\'on veux ici, on voudrait trouver un code qui prends la valeur de 'n', \nla multiplie par 2, et place ce resultat dans 'n'.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            if(a[i] == stu_ans): #same
                self.assertEqual(corr_ans, stu_ans, anssame.format(a[i],corr_ans,stu_ans))
            if(2 == stu_ans): # 2 != twice
                self.assertEqual(corr_ans, stu_ans, anstwo.format(a[i],corr_ans,stu_ans))    
            else: 
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))



if __name__ == '__main__':
    unittest.main()

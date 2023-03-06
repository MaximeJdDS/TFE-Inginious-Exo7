#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'aire'), _("Tu n\'as pas defini la bonne fonction. La fonction 'air' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(2, 169) for _ in range(15)]
        b = [random.randint(2, 169) for _ in range(15)]
        ansresult   = _("Pour une longueur de {} et une largeur de {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        ansplus   = _("Pour une longueur de {} et une largeur de {} la réponse attendu est {} et ta fonction a renvoyé {}. \nIl semblerait que tu as fait la somme des 2 valeurs. \nUne surface se calcul comment déjà ?")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i],b[i])
            corr_ans = corr.fonction(a[i],b[i])
            
            if((stu_ans != corr_ans)and(stu_ans == a[i]+b[i])):
                self.assertEqual(corr_ans, stu_ans, ansplus.format(a[i],b[i],corr_ans,stu_ans))
            else :
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],b[i],corr_ans,stu_ans))

    


if __name__ == '__main__':
    unittest.main()

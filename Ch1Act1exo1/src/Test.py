#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    
    def test_result_Int(self):
        a = [random.randint(1, 100) for _ in range(5)]
        b = [random.randint(1, 100) for _ in range(5)]
        ansresult   = _("Pour un rectangle de longueur: {} et de largeur: {}, la réponse attendu est {} et ta fonction a renvoyé {}.\n Pour multiplier en Python il faut utiliser le symbole  *  .")
        ansUnmodified = _("La variable 'aire' n'a pas été instanciée.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i],b[i])
            corr_ans = corr.fonction(a[i],b[i])
            if(stu_ans == -123456543): #aire non modifiée
                self.assertEqual(0, 1, ansUnmodified)
            else: 
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],b[i],corr_ans,stu_ans))



if __name__ == '__main__':
    unittest.main()

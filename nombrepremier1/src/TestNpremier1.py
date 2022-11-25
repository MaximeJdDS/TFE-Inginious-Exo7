#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrNpremier1 as corr
import npremier1


class TestNpremier1(unittest.TestCase):
    
    def test_npremier(self):
        a = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47] #,53,59,61,67,71,73,79,83,89,97]
        ansPair   = _("Le nombre {} est un nombre premier et tu as renvoyé {} .")
        for i in range(len(a)):
            stu_ans  = npremier1.est_premier_1(a[i])
            corr_ans = corr.est_premier_1(a[i])
            self.assertEqual(corr_ans, stu_ans, ansPair.format(a[i],stu_ans))
            

    def test_nNonpremier(self):
        a = [random.randint(4, 50) for _ in range(5)]
        ansPair   = _("Le nombre {} est un nombre premier et tu as renvoyé {} .")
        ansUnpair = _("Le nombre {} n est pas un nombre premier et tu as renvoyé {} .")
        for i in range(len(a)):
            stu_ans  = npremier1.est_premier_1(a[i])
            corr_ans = corr.est_premier_1(a[i])
            if(corr_ans): #Nombre premier
                self.assertEqual(corr_ans, stu_ans, ansPair.format(a[i],stu_ans))
            else:         #Nombre pas premier
                self.assertEqual(corr_ans, stu_ans, ansUnpair.format(a[i],stu_ans))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corrppdiv as corr
import ppdiv


class Testppdiv(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(ppdiv, 'plus_petit_diviseur'), _("Tu n as pas defini la bonne fonction. La fonction 'plus_petit_diviseur' est introuvable."))

    def test_ppdiv(self):
        a = [random.randint(1, 150) for _ in range(5)]
        ansPair   = _("Le plus petit diviseur de {} est {} et tu as renvoyé {}.")
        for i in range(len(a)):
            stu_ans  = ppdiv.plus_petit_diviseur(a[i])
            corr_ans = corr.plus_petit_diviseur(a[i])
            self.assertEqual(corr_ans, stu_ans, ansPair.format(a[i],corr_ans,stu_ans))
            

    


if __name__ == '__main__':
    unittest.main()

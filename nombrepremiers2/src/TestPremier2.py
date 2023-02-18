#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrPremier2 as corr
import premier2


class TestPrime2(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(pair, 'est_premier2'), _("Tu n\'as pas défini la bonne fonction. La fonction 'est_premier2' est introuvable."))

    def test_prime2(self):
        a = [random.randint(1, 100) for _ in range(10)]
        ansNotPrime   = _("L\' entier {} n\'est pas premier. Pourtant ta fonction a retourné {}.")
        ansPrime      = _("L\' entier {} est premier. Pourtant ta fonction a retourné {}.")
        for i in range(len(a)):
            stu_ans  = pair.est_premier2(a[i])
            corr_ans = corr.est_premier2(a[i])
            if(corr_ans): #Prime
                self.assertEqual(corr_ans, stu_ans, ansPrime.format(a[i],stu_ans))
            else: #NotPrime
                self.assertEqual(corr_ans, stu_ans, ansNotPrime.format(a[i],stu_ans))



if __name__ == '__main__':
    unittest.main()

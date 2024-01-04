#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrPair as corr
import pair


class TestPair(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(pair, 'est_pair'), _("Tu n'as pas défini la bonne fonction. La fonction 'est_pair' est introuvable."))

    def test_pair(self):
        a = [random.randint(1, 69) for _ in range(5)]
        ansPair   = _("L entier {} est pair et vous avez retourné {}.")
        ansUnpair = _("L entier {} n'est pas pair et vous avez retourné {}.")
        for i in range(len(a)):
            stu_ans  = pair.est_pair(a[i])
            corr_ans = corr.est_pair(a[i])
            if(a[i]%2 == 0): #Pair
                self.assertEqual(corr_ans, stu_ans, ansPair.format(a[i],stu_ans))
            else: #Unpair
                self.assertEqual(corr_ans, stu_ans, ansUnpair.format(a[i],stu_ans))

    def test_negatif(self):
        a = [random.randint(-50, 0) for _ in range(5)]
        ansPair   = _("L entier {} est pair et vous avez retourné {}.")
        ansUnpair = _("L entier {} n'est pas pair et vous avez retourné {}.")
        for i in range(len(a)):
            stu_ans  = pair.est_pair(a[i])
            corr_ans = corr.est_pair(a[i])
            if(a[i]%2 == 0): #Pair
                self.assertEqual(corr_ans, stu_ans, ansPair.format(a[i],stu_ans))
            else:            #Unpair
                self.assertEqual(corr_ans, stu_ans, ansUnpair.format(a[i],stu_ans))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrDiv as corr
import Div
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(Div, 'est_divisible')):
    tagDico = Misconceptions.runAllFunc(Div.est_divisible)
Misconceptions.tagTransfer(tagDico)


class TestDiv(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(Div, 'est_divisible'), _("You did not provide the requested method."))

    def test_div(self):
        a = [random.randint(10, 100) for _ in range(5)]
        b = [random.randint(2, 15) for _ in range(5)]
        ans    = _("Le nombre a: {} est divisible par {} et vous avez renvoyé {}.")
        ansNeg = _("Le nombre a: {} n est pas divisible par {} et vous avez renvoyé {}.")
        for i in range(len(a)):
            stu_ans  = Div.est_divisible(a[i],b[i])
            corr_ans = corr.est_divisible(a[i],b[i])
            if(a[i]%b[i] == 0): #a est div par b
                self.assertEqual(corr_ans, stu_ans, ans.format(a[i],b[i],stu_ans))
            else: #a n'est pas div par b
                self.assertEqual(corr_ans, stu_ans, ansNeg.format(a[i],b[i],stu_ans))


if __name__ == '__main__':
    unittest.main()
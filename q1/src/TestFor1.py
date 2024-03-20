#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import CorrFor1 as corr
import for1
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(for1, 'quotient_reste')):
    tagDico = Misconceptions.runAllFunc(for1.quotient_reste)
Misconceptions.tagTransfer(tagDico)


class TestFor1(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(for1, 'quotient_reste'), _("Tu ne dois pas avoir implementé la bonne methode, quotien_reste(a,b) est introuvable."))

    def test_For1(self):
        a = [random.randint(10, 100) for _ in range(5)]
        b = [random.randint(2, 15) for _ in range(5)]
        ans = _("Le maximum de {} est {} et vous avez renvoyé {}.")
        for i in range(len(a)):
            with io.StringIO() as out, redirect_stdout(out):
                for1.quotient_reste(a[i], b[i])
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.quotient_reste(a[i], b[i])
                corr_ans = out.getvalue()
            self.assertEqual(corr_ans, stu_ans, ans.format([a[i], b[i]], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()

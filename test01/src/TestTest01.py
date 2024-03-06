#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import CorrTest01 as corr
import max
import Misconceptions

tagDico = Misconceptions.runAllFunc(max.f)

def tagTransfer():
        for tag in tagDico :
            print(f"TAG:{tag}=True")

class TestSum(unittest.TestCase):
    

    def test_sum(self):
        stu_ans = max.f()
        ans = _("Vous avez renvoyé {}.\nAlors que {} était attendu.")
        tagTransfer()
        self.assertEqual(True, stu_ans, ans.format(stu_ans,True))
            

    

if __name__ == '__main__':
    try:
        unittest.main()
    finally:
        tagTransfer()

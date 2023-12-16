#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student

def comparer_tableaux(tab1, tab2, n):
    diff1 = sorted(list(set(tab1) - set(tab2)))[:n]
    diff2 = sorted(list(set(tab2) - set(tab1)))[:n]
    return diff1, diff2

class Test(unittest.TestCase):
    

    def test_result_Int(self):        
        ansresult   = _("\nIl te manque au moins les éléments suivants :\n{} \nEt tu as mis en trop dans le sac au moins les éléments suivants:\n{} \n.")
        stu_ans  = sorted(student.fonction())
        corr_ans = corr.fonction()
        lack,over = comparer_tableaux(corr_ans,stu_ans,3)
        self.assertEqual(corr_ans, stu_ans, ansresult.format(lack,over))
        

    

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'mergeTimes'), _("Tu n\'as pas défini la bonne fonction. La fonction 'mergeTimes' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 5) for _ in range(5)]
        b = [random.randint(1, 5) for _ in range(5)]
        
        ansresult   = _("Pour l'appel mergeTimes({},{},{},{}) \nla réponse attendu est {} \net ta fonction a renvoyé {}.")
        ansUnpair = _("L entier {} n est pas pair.")
        for i in range(len(a)):
            tab1 = [random.randint(-10, 10) for _ in range(a[i])]
            tab2 = [random.randint(-10, 10) for _ in range(b[i])]
            stu_ans  = student.fonction(tab1,a[i],tab2,b[i])
            corr_ans = corr.fonction(tab1,a[i],tab2,b[i])
            
            self.assertEqual(corr_ans, stu_ans, ansresult.format(tab1,a[i],tab2,b[i],corr_ans,stu_ans))
            

    

if __name__ == '__main__':
    unittest.main()

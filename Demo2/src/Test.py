#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico = Misconceptions.runAllFunc(student.fonction)
Misconceptions.tagTransfer(tagDico)
class Test(unittest.TestCase):
    

    def test_result_Int(self):
        a = [random.randint(-100, 100) for _ in range(20)]
        ansresult   = _("Pour l\'élément {} contenu dans ``n`` la réponse attendu est {} et ta fonction a renvoyé {}.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            
            if(a[i]< 0): #Négatif
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            else: #Positif
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))

    


if __name__ == '__main__':
    unittest.main()

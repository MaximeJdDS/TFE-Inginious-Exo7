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
        a = [random.randint(0, 13) for _ in range(5)]
        ansresult   = _("Pour n = {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        ansresultMinusOne   = _("Ton code renvoye {} pour l'entré n = {}. Il faut stocker ta réponse dans la variable ``result``.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            if(stu_ans == -1):
                self.assertEqual(corr_ans, stu_ans, ansresultMinusOne.format(stu_ans,a[i]))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            

    


if __name__ == '__main__':
    unittest.main()

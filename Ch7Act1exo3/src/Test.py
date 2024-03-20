#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'somme')):
    tagDico = Misconceptions.runAllFunc(student.somme)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'somme'), _("Tu n\'as pas defini la bonne fonction. La fonction 'somme' est introuvable."))

    def test_result_Int(self):
        
        ansresult   = _("Pour le tableau:\n{} \nla réponse attendu est {} et ta fonction a renvoyé {}.")
        for i in range(10):
            lenght = random.randint(1,69) 
            a = [random.randint(-100, 100) for _ in range(lenght)]            
            stu_ans  = student.fonction(a)
            corr_ans = corr.fonction(a)
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a,corr_ans,stu_ans))
            




if __name__ == '__main__':
    unittest.main()

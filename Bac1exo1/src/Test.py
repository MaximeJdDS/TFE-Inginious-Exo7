#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'filtreTableau')):
    tagDico = Misconceptions.runAllFunc(student.filtreTableau)
#Misconceptions.tagTransfer(tagDico)

class Test(unittest.TestCase):
    def test_exists(self):
        Misconceptions.tagTransfer(tagDico)
        self.assertTrue(hasattr(student, 'filtreTableau'), _("Tu n\'as pas defini la bonne fonction. La fonction 'filtreTableau' est introuvable."))
        

    def test_result_Int(self):
        
        ansresult   = _("Pour le tableau: {}\nEt le filtre: {}\nLa réponse attendue est {}\n et ta fonction a renvoyée {}.")
        
        for i in range(5):
            a = [random.randint(1, 10) for _ in range(10)]
            b = [random.randint(1, 10) for _ in range(3)]
            stu_ans  = student.fonction(a,b)
            corr_ans = corr.fonction(a,b)
            Misconceptions.tagTransfer(tagDico)
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a,b,corr_ans,stu_ans))
            

    


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'MatrixReduc')):
    tagDico = Misconceptions.runAllFunc(student.MatrixReduc)




class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'MatrixReduc'), _("Tu n\'as pas défini la bonne fonction. La fonction 'MatrixReduc' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 10) for _ in range(10)]
        ansresult   = _("Pour la matrice = {}, \nla réponse attendue est {} \net ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            low = 0
            high = 20
            cols = (2*i)+2
            rows = (2*i)+2

            matrix = [random.choices(range(low,high), k=cols) for _ in range(rows)]
            
            
            stu_ans  = student.fonction(matrix)
            corr_ans = corr.fonction(matrix)
            
            Misconceptions.tagTransfer(tagDico)
            
            self.assertEqual(corr_ans, stu_ans, ansresult.format(matrix,corr_ans,stu_ans))
            
    


if __name__ == '__main__':    
    unittest.main()
    
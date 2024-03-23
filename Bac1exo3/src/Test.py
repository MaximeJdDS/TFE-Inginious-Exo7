#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'MatrixCheck')):
    tagDico = Misconceptions.runAllFunc(student.MatrixCheck)




class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'MatrixCheck'), _("Tu n\'as pas défini la bonne fonction. La fonction 'MatrixCheck' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 10) for _ in range(10)]
        ansresult   = _("Pour la matrice = {}, \net f renvoyant {},\nla réponse attendue est {} et ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            low = 0
            high = 10
            cols = 5
            rows = 5

            matrix = [random.choices(range(low,high), k=cols) for _ in range(rows)]
            
            
            #student.passValeur(a[i])
            #corr.passValeur(a[i])
            stu_ans  = student.fonction(matrix)
            corr_ans = corr.fonction(matrix)
            if(Misconceptions.ParenthesesOnlyIfArgument(student.MatrixCheck,['f'])):
                tagDico.append('ParenthesesOnlyIfArgument')
            Misconceptions.tagTransfer(tagDico)
            
            self.assertEqual(corr_ans, stu_ans, ansresult.format(matrix,[0,1,2],corr_ans,stu_ans))
            
    def test_result(self):
        a = [random.randint(1, 10) for _ in range(3)]
        ansresult   = _("Pour la matrice = {}, \net f renvoyant {},\nla réponse attendue est {} et ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            low = 1
            high = 100
            cols = 5
            rows = 5

            matrix = [random.choices(range(low,high), k=cols) for _ in range(rows)]
            
            
            #student.passValeur(a[i])
            #corr.passValeur(a[i])
            stu_ans  = student.fonction(matrix)
            corr_ans = corr.fonction(matrix)
            if(Misconceptions.ParenthesesOnlyIfArgument(student.MatrixCheck,['f'])):
                tagDico.append('ParenthesesOnlyIfArgument')
            Misconceptions.tagTransfer(tagDico)
            
            self.assertEqual(corr_ans, stu_ans, ansresult.format(matrix,[0,1,2],corr_ans,stu_ans))


if __name__ == '__main__':    
    unittest.main()
    
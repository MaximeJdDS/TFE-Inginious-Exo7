#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q
import Misconceptions

#tagDico=["MissnamingFunction"]
#if(hasattr(q, 'plus_frequent')):
tagDico = Misconceptions.runAllFunc(q.rainfall)
#Misconceptions.tagTransfer(tagDico)

class TestQ(unittest.TestCase):
    
    def test_one(self):
        Misconceptions.tagTransfer(tagDico)
        feedback = _("Pour la liste {},\nla réponse attendue était {} et ta fonction a renvoyé {}.")
        test = [3, 5, -2, 4, 9999, 10]
        stu_ans = q.rainfall(test)
        corr_ans = corr.rainfall(test)
        self.assertEqual(corr_ans, stu_ans, feedback.format(test,corr_ans,stu_ans))
        
    def test_serious(self):
        Misconceptions.tagTransfer(tagDico)
        feedback = _("Pour la liste {},\nla réponse attendue était {} et ta fonction a renvoyé {}.")
        for i in range(5):
            test = [random.randint(-100, 500) for _ in range(10)]         
            b = random.randint(0, 9)
            test[b] = 9999
            stu_ans = q.rainfall(test)
            corr_ans = corr.rainfall(test)
            self.assertEqual(corr_ans, stu_ans, feedback.format(test,corr_ans,stu_ans))    


if __name__ == '__main__':
    unittest.main()

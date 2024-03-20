#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
tagDico=["MissnamingFunction"]
if(hasattr(student, 'majLock')):
    tagDico = Misconceptions.runAllFunc(student.majLock)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'majLock'), _("Tu n\'as pas defini la bonne fonction. La fonction 'majLock' est introuvable."))

    def test_CasDeBase(self):
        #a = [random.randint(65, 90) for _ in range(15)]
        a = ["pETIT TEXTE", "abcDE", "j'AI TOUT ECRIS EN mAJlOCK"]
        ansresult   = _("Pour le texte {} \n la réponse attendu est {}\n et ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            
            
    
    


if __name__ == '__main__':
    unittest.main()

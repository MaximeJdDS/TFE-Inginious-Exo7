#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions
tagDico=["MissnamingFunction"]
if(hasattr(student, 'minuscule')):
    tagDico = Misconceptions.runAllFunc(student.minuscule)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'minuscule'), _("Tu n\'as pas défini la bonne fonction. La fonction 'minuscule' est introuvable."))

    def test_CasDeBase(self):
        a = [random.randint(65, 90) for _ in range(15)]
        ansresult   = _("Pour l\'élément {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(chr(a[i]))
            corr_ans = corr.fonction(chr(a[i]))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(chr(a[i]),corr_ans,stu_ans))
            
            
    def test_CasSpecial(self):
        a = [random.randint(33, 64) for _ in range(10)]
        ansresult   = _("Pour l\'élément {}, la réponse attendue est {} et ta fonction a renvoyé {}. \n Qu'est-ce qu'on fait quand il y a des cas oú l'on voudrait faire quelque chose mais pour un autre cas, autre chose ?")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(chr(a[i]))
            corr_ans = corr.fonction(chr(a[i]))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(chr(a[i]),corr_ans,stu_ans))

    


if __name__ == '__main__':
    unittest.main()

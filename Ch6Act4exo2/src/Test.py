#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions
tagDico=["MissnamingFunction"]
if(hasattr(student, 'switch')):
    tagDico = Misconceptions.runAllFunc(student.switch)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'switch'), _("Tu n\'as pas defini la bonne fonction. La fonction 'switch' est introuvable."))

    def test_CasDeBase(self):
        a = [random.randint(65, 90) for _ in range(15)]
        a = a + [random.randint(97, 122) for _ in range(15)]
        ansresult   = _("Pour l\'élément {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(chr(a[i]))
            corr_ans = corr.fonction(chr(a[i]))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(chr(a[i]),corr_ans,stu_ans))
            
            
    def test_CasSpecial(self):
        a = [random.randint(33, 127) for _ in range(50)]
        ansresult   = _("Pour l\'élément {} la réponse attendu est {} et ta fonction a renvoyé {}.\n Tu as déjà du régler ce problème avec minuscule(c).\n Tu as 2 solutions, soit tu fais comme minuscule, soit tu utilises minuscule(c) pour régler ce problème.")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(chr(a[i]))
            corr_ans = corr.fonction(chr(a[i]))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(chr(a[i]),corr_ans,stu_ans))

    


if __name__ == '__main__':
    unittest.main()

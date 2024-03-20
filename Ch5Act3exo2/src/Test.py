#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'nombres_jumeaux_apres')):
    tagDico = Misconceptions.runAllFunc(student.nombres_jumeaux_apres)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'nombres_jumeaux_apres'), _("Tu n\'as pas défini la bonne fonction. La fonction 'nombres_jumeaux_apres' est introuvable."))

    def test_result(self):
        a = [random.randint(1000,10000) for _ in range(5)]
        ansresult   = _("Pour l'élément {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        ansPlus2    = _("Pour l'élément {} la réponse attendu est {} et ta fonction a renvoyé {}. N'oublie pas qu'on demande p tel que p et p+2 soient jumeaux. On attends que p soit renvoyé, pas p+2.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            if(corr_ans+2 == stu_ans):
                self.assertEqual(corr_ans, stu_ans, ansPlus2.format(a[i],corr_ans,stu_ans))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
                
    


if __name__ == '__main__':
    unittest.main()
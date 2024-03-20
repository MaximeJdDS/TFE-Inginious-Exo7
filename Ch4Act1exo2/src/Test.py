#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'soustraction')):
    tagDico = Misconceptions.runAllFunc(student.soustraction)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'soustraction'), _("Tu n\'as pas defini la bonne fonction. La fonction 'soustraction' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 569) for _ in range(25)]
        b = [random.randint(1, 569) for _ in range(25)]
        ansresult   	= _("Pour les éléments {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        ansresultSwap   = _("Pour les éléments {} la réponse attendu est {} et ta fonction a renvoyé {}.\n Attention à bien vérifier l'ordre des arguments. Ici a-b n'est pas toujours égal à b-a.")
        for i in range(len(a)):
            stu_ans  = student.soustraction(a[i],b[i])
            corr_ans = corr.fonction(a[i],b[i])
            if((stu_ans != corr_ans) and (a[i] - b[i]) == stu_ans ): #Swap
                self.assertEqual(corr_ans, stu_ans, ansresultSwap.format([a[i],b[i]],corr_ans,stu_ans))
            else: 
                self.assertEqual(corr_ans, stu_ans, ansresult.format([a[i],b[i]],corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

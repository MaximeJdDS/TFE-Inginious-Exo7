#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'troisieme')):
    tagDico = Misconceptions.runAllFunc(student.troisieme)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'troisieme'), _("Tu n\'as pas defini la bonne fonction. La fonction 'troisieme(tab)' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 1000) for _ in range(5)]
        ansresult   = _("Pour le tableau d'entrée : {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        ansresult3   = _("Pour le tableau d'entrée : {} la réponse attendu est {} et ta fonction a renvoyé {}. \nLe troisième élément pour nous n'est pas forcément à l'emplacement 3. \nReregarde le tableau ci-dessus pour connaitre le rang de chacune des cases du tableau.")
        
        stu_ans  = student.fonction(a)
        corr_ans = corr.fonction(a)
        if(stu_ans == a[3] and stu_ans != a[2]): 
            self.assertEqual(corr_ans, stu_ans, ansresult3.format(a,corr_ans,stu_ans))
        else: 
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a,corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

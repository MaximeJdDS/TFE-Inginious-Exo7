#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'est_pair'), _("Tu n\'as pas defini la bonne fonction. La fonction 'est_pair' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 69) for _ in range(5)]
        ansresult   = _("Pour l\'élément {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        ansUnpair = _("L entier {} n est pas pair.")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            if(a[i]%2 == 0): #Pair
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            else: #Unpair
                self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))

    def test_result_String(self):
        a = ["chat","chien","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","le"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

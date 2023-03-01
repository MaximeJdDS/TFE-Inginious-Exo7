#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'distance_hamming'), _("Tu n\'as pas defini la bonne fonction. La fonction 'distance_hamming' est introuvable."))

    

    def test_result_String(self):
        a = ["japon","tout pareil","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","Satin"]
        b = ["savon","tout pareil","mots TresTresLongPourVoirSiLeSVaBienALaFinDuMot","Lapin"]
        ansresult   = _("Pour le couple de mots \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i],b[i])
            corr_ans = corr.fonction(a[i],b[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format([a[i],b[i]],corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

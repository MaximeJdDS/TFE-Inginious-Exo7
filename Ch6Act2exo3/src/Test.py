#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'verlan')):
    tagDico = Misconceptions.runAllFunc(student.verlan)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'verlan'), _("Tu n\'as pas defini la bonne fonction. La fonction 'verlan' est introuvable."))

    

    def test_result_String(self):
        a = ["chat","chien","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","tocard","louche"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

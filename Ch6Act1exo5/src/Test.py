#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'affiche_conjugaison')):
    tagDico = Misconceptions.runAllFunc(student.affiche_conjugaison)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'affiche_conjugaison'), _("Tu n\'as pas defini la bonne fonction. La fonction 'affiche_conjugaison' est introuvable."))

    

    def test_result_String(self):
        a = ["chanter","danser","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMoter","dessiner"]
        ansresult   = _("Pour le verbe \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            
    def test_print(self):
        a = ["chanter","danser","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMoter","dessiner"]
        ans  = _("Pour le verbe \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            with io.StringIO() as out, redirect_stdout(out):
                student.fonction(a[i])
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.fonction(a[i])
                corr_ans = out.getvalue()
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))        

    def test_print_hors_premier_groupe(self):       
        a = ["finir","cuire","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","instruire"]
        ans  = _("Pour le verbe \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            with io.StringIO() as out, redirect_stdout(out):
                student.fonction(a[i])
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.fonction(a[i])
                corr_ans = out.getvalue()
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))         

if __name__ == '__main__':
    unittest.main()

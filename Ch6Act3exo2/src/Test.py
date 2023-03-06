#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'position_de_AT'), _("Tu n\'as pas defini la bonne fonction. La fonction 'position_de_AT' est introuvable."))

    

    def test_result_String(self):
        a = ["CTTATGCT","GATATAT","GACCGTA","GACCGTAGACCGTAGACCGTAGACCGTAGACCGTAGACCGTAGACCGTA","GACCGTAGACCGTAGACCGTAGACCGTATGACCGTA"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

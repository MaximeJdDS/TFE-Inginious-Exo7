#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'nombre_germain_apres'), _("Tu n\'as pas défini la bonne fonction. La fonction 'nombre_germain_apres(n)' est introuvable."))

    def test_result(self):
        a = [random.randint(1000,10000) for _ in range(5)]
        ansresult   = _("Pour l'élément {} la réponse attendu est {} et ta fonction a renvoyé {}.")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
                
    


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    

    def test_result_Int(self):
        
        ansresult      = _("La valeur attendue est {} et ta variable demo contient : {}.")
        ansNotInstance = _("Il semblerait que tu n'as pas instancié la variable nommé :\n demo, relis l'énoncé en ayant en tête que tu ne dois pas avoir \n NomDeVariable écris dans ton code.")
        
        stu_ans  = student.fonction()
        corr_ans = corr.fonction()
        if(stu_ans == "Pas instancié"):
            self.assertEqual(corr_ans, stu_ans, ansNotInstance.format())
        else :
            self.assertEqual(corr_ans, stu_ans, ansresult.format(corr_ans,stu_ans))
            

    


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student


class Test(unittest.TestCase):
    

    def test_result_Int(self):
        a = [random.randint(97, 122) for _ in range(15)] #97 to 122
        ansresult   = _("Pour la lettre {} la réponse attendu est {} et ta fonction a renvoyé {}. \n Regarde bien le tableau et trouve ce qui différencie une lettre minuscule de sa majuscule.")
        
        for i in range(len(a)):
            stu_ans  = student.fonction(chr(a[i]))
            corr_ans = corr.fonction(chr(a[i]))
            self.assertEqual(corr_ans, stu_ans, ansresult.format(chr(a[i]),corr_ans,stu_ans))
            
    


if __name__ == '__main__':
    unittest.main()

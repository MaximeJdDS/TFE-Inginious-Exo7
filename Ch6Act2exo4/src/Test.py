#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'est_un_palindrome')):
    tagDico = Misconceptions.runAllFunc(student.est_un_palindrome)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'est_un_palindrome'), _("Tu n\'as pas defini la bonne fonction. La fonction 'est_un_palindrome' est introuvable."))

    

    def test_result_palindrome(self):
        a = ["ressasser","radar","kayak","sus","snobons","UwU","elle"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))

    def test_result_non_palindrome(self):
        a = ["palindrome","mot","chien","chat","voyage","qwertyuiopMNpoiuytrewq"]
        ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
        for i in range(len(a)):
            stu_ans  = student.fonction(a[i])
            corr_ans = corr.fonction(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrFermat as corr
import Fermat

def estpremier(n): 
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0: return False
        return True

def isFermat(n):
    i    = 1
    temp = corr.F(i)
    while temp < n:
        i = i+1
        temp = corr.F(i)
    if temp == n : return True
    else : return False


class TestFermat(unittest.TestCase):
    
    
    def test_Fermat_exists(self):
        self.assertTrue(hasattr(Fermat, 'F'), _("Tu n\'as pas defini la bonne fonction. La fonction \'F(n)\' est introuvable."))
        
    def test_ContreExemple_exists(self):
        self.assertTrue(hasattr(Fermat, 'contreExemple'), _("Tu n\'as pas defini la bonne fonction. La fonction \'contreExemple()\' est introuvable."))

    def test_Fermat(self):
        a = [random.randint(1, 3) for _ in range(2)]
        ansFermat   = _("Le {} ieme nombre de Fermat est {} et tu as renvoyé {}.")
        #ansUnpair = _("L entier {} n est pas pair.")
        for i in range(len(a)):
            stu_ans  = Fermat.F(a[i])
            corr_ans = corr.F(a[i])
            self.assertEqual(corr_ans, stu_ans, ansFermat.format(a[i],corr_ans,stu_ans))
            

    def test_Prime(self):
        ansPrime   = _("Ta fonction a renvoyé {}. Ce nombre est premier. Pour rappel, on cherche le premier nombre de Fermat qui n'est pas premier. N'hesite pas à utiliser la fonction \'estpremier(n)\'.")
        ansNotFermat = _("Ta fonction a renvoyé {}. Ce nombre n'est pas un nombre de Fermat. Pour rappel, on cherche le premier nombre de Fermat qui n'est pas premier. N'hesite pas a utiliser la fonction \'F(n)\' que tu as défini précédemment.")
        stu_ans  = Fermat.contreExemple()
        corr_ans = corr.contreExemple()
        if not (isFermat(stu_ans)):
            self.assertEqual(corr_ans, stu_ans, ansNotFermat.format(stu_ans))
        if estpremier(stu_ans):
            self.assertEqual(corr_ans, stu_ans, ansPrime.format(stu_ans))

if __name__ == '__main__':
    unittest.main()

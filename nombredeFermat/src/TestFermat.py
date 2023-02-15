#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrFermat as corr
import Fermat


#code found at https://geekflare.com/prime-number-in-python/
def est_premier(n): 
	for i in range(2,int(math.sqrt(n))+1):
		if (n%i) == 0:
			return False
	return True

class TestFermat(unittest.TestCase):
    
    def test_Fermat_exists(self):
        self.assertTrue(hasattr(Fermat, 'F'), _("Tu n\'as pas defini la bonne fonction. La fonction \'F(n)\' est introuvable."))
        
    def test_ContreExemple_exists(self):
        self.assertTrue(hasattr(Fermat, 'contreExemple'), _("Tu n\'as pas defini la bonne fonction. La fonction \'contreExemple()\' est introuvable."))

    def test_Fermat(self):
        a = [random.randint(1, 20) for _ in range(8)]
        ansFermat   = _("Le {} ieme nombre de Fermat est {} et tu as renvoyé {}.")
        #ansUnpair = _("L entier {} n est pas pair.")
        for i in range(len(a)):
            stu_ans  = Fermat.F(a[i])
            corr_ans = corr.F(a[i])
            self.assertEqual(corr_ans, stu_ans, ansFermat.format(a[i],corr_ans,stu_ans))
            

    def test_Prime(self):
        ansPrime   = _("Le premier nombre de Fermat qui n'est pas premier est {}, ta fonction a renvoyé {}.")
        for i in range(len(a)):
            stu_ans  = Fermat.contreExemple()
            corr_ans = corr.contreExemple()
            self.assertEqual(corr_ans, stu_ans, ansPrime.format(corr_ans,stu_ans))
            


if __name__ == '__main__':
    unittest.main()

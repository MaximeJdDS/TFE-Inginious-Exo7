#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student

def equals(a,b,proportionA):
    if( ((a*(1-proportionA))<= b) and ((a*(1+proportionA))>= b)):
        return True
    else : 
        return False
    

class Test(unittest.TestCase): 
    def test_exists(self):
        self.assertTrue(hasattr(student, 'benchmark'), _("Tu n\'as pas defini la bonne fonction. La fonction 'benchmark' est introuvable."))
        self.assertTrue(hasattr(student, 'est_premier_1'), _("Tu n\'as pas defini la bonne fonction. La fonction 'est_premier_1' est introuvable."))
        self.assertTrue(hasattr(student, 'est_premier_2'), _("Tu n\'as pas defini la bonne fonction. La fonction 'est_premier_2' est introuvable."))
        self.assertTrue(hasattr(student, 'est_premier_3'), _("Tu n\'as pas defini la bonne fonction. La fonction 'est_premier_3' est introuvable."))

        
    def test_prime2(self):
        a = [random.randint(1, 500) for _ in range(20)]
        ansNotPrime   = _("L\' entier {} n\'est pas premier. Pourtant ta fonction numero {} a retourné {}.")
        ansPrime      = _("L\' entier {} est premier. Pourtant ta fonction numero {} a retourné {}.")
        
        for i in range(len(a)):
            stu_ans  = student.est_premier_1(a[i])
            corr_ans = corr.est_premier_1(a[i])
            if(corr_ans): #Prime
                self.assertEqual(corr_ans, stu_ans, ansPrime.format(a[i],1,stu_ans))
            else: #NotPrime
                self.assertEqual(corr_ans, stu_ans, ansNotPrime.format(a[i],1,stu_ans))
                
        for i in range(len(a)):
            stu_ans  = student.est_premier_2(a[i])
            corr_ans = corr.est_premier_2(a[i])
            if(corr_ans): #Prime
                self.assertEqual(corr_ans, stu_ans, ansPrime.format(a[i],2,stu_ans))
            else: #NotPrime
                self.assertEqual(corr_ans, stu_ans, ansNotPrime.format(a[i],2,stu_ans))
                
        for i in range(len(a)):
            stu_ans  = student.est_premier_3(a[i])
            corr_ans = corr.est_premier_3(a[i])
            if(corr_ans): #Prime
                self.assertEqual(corr_ans, stu_ans, ansPrime.format(a[i],3,stu_ans))
            else: #NotPrime
                self.assertEqual(corr_ans, stu_ans, ansNotPrime.format(a[i],3,stu_ans))



        
        
    def test_result(self):
        
        ansresultPlus   = _("Pour le est_premier {} la réponse attendu est plus grande que ce que ta fonction a renvoyé. Ta fonction a renvoyé {}.")
        ansresultMoins   = _("Pour le est_premier {} la réponse attendu est plus petite que ce que ta fonction a renvoyé. Ta fonction a donc pris trop de temps. Ta fonction a renvoyé {}.")       
        stu_ans  = student.fonction()
        corr_ans = corr.fonction()
        proportion = 0.05
        for i in range(len(corr_ans)):
            intervalBool=equals(corr_ans,stu_ans,proportion)
            if(stu_ans[i]>corr_ans[i]):
                self.assertEqual(True, intervalBool, ansresultMoins.format(i+1,corr_ans,stu_ans))
            else :
                self.assertEqual(True, intervalBool, ansresultMoins.format(i+1,corr_ans,stu_ans))
        

    


if __name__ == '__main__':
    unittest.main()

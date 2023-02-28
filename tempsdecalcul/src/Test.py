#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student

def equals(a,b,biais):
    if( ((a*(1.0-biais))<= b) and ((a*(1.0+biais))>= b)):
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
        a = [random.randint(100, 500) for _ in range(20)]
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
        
        #ansresultMoins  = _("Pour le est_premier {}. Ta fonction a été trop rapide. Ta fonction a pris {} secondes.")
        ansresultPlus   = _("Pour le est_premier {}. Ta fonction a pris trop de temps. Ta fonction a pris {} secondes.")       
        stu_ans  = student.fonction()
        corr_ans = corr.fonction()
        biais = 0.2 # 20%
        for i in range(len(corr_ans)-1):
            intervalBool=equals(corr_ans[i+1],stu_ans[i+1],biais)
            if(stu_ans[i+1]>corr_ans[i+1]): #Student takes too much times
                self.assertEqual(True, intervalBool, ansresultPlus.format(i+2,corr_ans[i+1],stu_ans[i+1]))
                
            
            #else :                      #Student is too quick.
            #    if(i==0): #for est_premier2
            #        self.assertEqual(True, intervalBool, ansresultMoins.format(i+2,corr_ans[i+1],stu_ans[i+1]))
        

    


if __name__ == '__main__':
    unittest.main()

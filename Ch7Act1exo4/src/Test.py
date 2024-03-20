#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'pythagore')):
    tagDico = Misconceptions.runAllFunc(student.pythagore)
Misconceptions.tagTransfer(tagDico)

def pythagoreInt(n):
    database=[]
    for i in range(n):
        if i == 0 : continue
        for j in range(n):
            if j == 0 : continue
            if((math.sqrt(i**2 + j**2).is_integer())):
                temp=[i,j,int(math.sqrt(i**2 + j**2))]
                temp.sort()
                if temp not in database :
                    database.append(temp)
    return database                


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'pythagore'), _("Tu n\'as pas defini la bonne fonction. La fonction 'pythagore' est introuvable."))

    def test_result_Int(self):
        database100 = pythagoreInt(100)
        lenght = random.randint(5,10)
        a = []
        for i in range(lenght):
            b = [random.randint(2,50),random.randint(2,50)]
            if(random.randint(1,100)%3 == 0):
                indice = random.randint(0,len(database100)-1)
                b = database100[indice]
            else:
                b = b + [random.randint(5,70)]
                b.sort()
            a.append(b)
            
        ansresult   = _("Pour l\'élément {} \nla réponse attendu est \n{} \net ta fonction a renvoyé \n{}.")
        
        
        stu_ans  = student.fonction(a)
        corr_ans = corr.fonction(a)
            
        self.assertEqual(corr_ans, stu_ans, ansresult.format(a,corr_ans,stu_ans))
            



if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from inginious import feedback
import inginious_container_api.input as ingi_input
import inginious_container_api.feedback as ingi_feedback
import Misconceptions

import Corr as corr
import student

tagDico = Misconceptions.runAllFunc(student.fonction)

class Test(unittest.TestCase):
    
#    def test_FeedBack(self):
#        ingi_feedback.set_problem_feedback("Query: \n", 'q1', append=True)
#        stu_ans  = student.fonction()
#        corr_ans = corr.fonction()
#        if(stu_ans != corr_ans):
            ## FEEDBACKS: 
#        	ingi_feedback.set_problem_feedback(" Il y a des erreurs dans votre code. \n", 'q1', append=True)
#        	ingi_feedback.set_problem_feedback("\n", 'q1', append=True)
#        	ingi_feedback.set_problem_feedback("\nFailed", 'q1', append=True)
#        	ingi_feedback.set_problem_result("failed", 'q1')
#        	ingi_feedback.set_global_result("failed")
            
    

    def test_result_Int(self):
        
        ansresult      = _("La valeur attendue est {} et ta variable demo contient : {}.")
        ansNotInstance = _("Il semblerait que tu n'as pas instancié la variable nommé :\n demo, \n Relis l'énoncé en ayant en tête que tu ne dois pas avoir \n NomDeVariable écris dans ton code.")
        
        stu_ans  = student.fonction()
        corr_ans = corr.fonction()
        Misconceptions.tagTransfer(tagDico)
        if(stu_ans == "Pas instancié"):
            self.assertEqual(corr_ans, stu_ans, ansNotInstance.format())
        else :
            self.assertEqual(corr_ans, stu_ans, ansresult.format(corr_ans,stu_ans))
            

    
if __name__ == '__main__':
    unittest.main()

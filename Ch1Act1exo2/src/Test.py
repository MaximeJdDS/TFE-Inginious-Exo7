#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student

from inginious import feedback
import inginious_container_api.input as ingi_input
import inginious_container_api.feedback as ingi_feedback


class Test(unittest.TestCase):
    
    def test_result_Int(self):
        a = [random.randint(70, 150) for _ in range(5)]
        b = [random.randint(1, 69) for _ in range(5)]
        ansLeftOk   = _("La variable gauche contient bien la bonne valeur. \nCependant, la variable droite ne contient pas la bonne valeur. \nPeut-être qu'une troisième variable serait utile.")
        ansRightOk = _("La variable droite contient bien la bonne valeur. \nCependant, la variable gauche ne contient pas la bonne valeur. \nPeut-être qu'une troisième variable serait utile.")
        ansNoOk = _("Gauche et droite ne contienne pas la bonne valeur. \nEssaie de régler un problème à la fois, occupe toi de gauche comme si c'était ton seul objectif. On s'occupera de droite après.")
        for i in range(len(a)):
            stu_ansL, stu_ansR  = student.fonction(a[i],b[i])
            corr_ansL,corr_ansR = corr.fonction(a[i],b[i])
            if(stu_ansL == corr_ansL): #Left Ok
                if(stu_ansR == corr_ansR): #Right Ok => Valid
                    self.assertEqual(1, 1, "Réponse valide.")
                else: #Right KO                    
                    #ingi_feedback.set_grade(50)
                    self.assertEqual(corr_ansR, stu_ansR, ansLeftOk)
            else: #Left KO
                if(stu_ansR == corr_ansR): #Right Ok
                    #ingi_feedback.set_grade(50)
                    self.assertEqual(corr_ansL, stu_ansL, ansRightOk)
                else: # Totaly invalid answer
                    self.assertEqual(corr_ansR, stu_ansR, ansNoOk)


if __name__ == '__main__':
    unittest.main()

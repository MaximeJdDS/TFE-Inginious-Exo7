#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import Corr as corr
import student
import Misconceptions

tagDico = Misconceptions.runAllFunc(student.fonction)
Misconceptions.tagTransfer(tagDico)


class Test(unittest.TestCase):
    

    def test_print(self):
        a = [random.randint(1, 20) for _ in range(25)]
        b = [random.randint(1, 20) for _ in range(25)]
        ans  = _("La réponse attendue pour les éléments suivants : a={}, b={}, n={} est \n{}Et votre code a affiché :\n {}")
        ans2 = _("Ta fonction n\'affiche rien. N'oublie pas que pour afficher quelque chose il faut faire appel à la fonction \'print()\'.\n Si tu as perdu les 2 print() donnés au début de l'exercice, tu peux rafraichir la page pour revoir l'énoncé de départ.")
        biais = 0
        for i in range(len(a)):
            biais = (biais +1)%2 
            n = a[i] * b[i] + biais
            with io.StringIO() as out, redirect_stdout(out):
                student.fonction(a[i], b[i], n)
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.fonction(a[i], b[i], n)
                corr_ans = out.getvalue()
            if(stu_ans == ''):  
                self.assertEqual(corr_ans, stu_ans, ans2)
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], b[i], n, corr_ans, stu_ans))
    
    
    


if __name__ == '__main__':
    unittest.main()

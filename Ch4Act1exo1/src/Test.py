#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import Corr as corr
import student


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'Hello_World'), _("Tu n\'as pas défini la bonne fonction. La fonction 'Hello_World()' est introuvable. \nN'hésite pas à relire la page 24 du syllabus."))

    

            
    def test_print(self):
        
        ans  = _("Ta fonction affiche : \"{}\" et il faut qu'elle affiche : \"{}\".")
        ansNoPrint = _("Ta fonction n\'affiche rien. N'oublie pas que pour afficher quelque chose il faut faire appel à la fonction \'print()\'.")
        
        with io.StringIO() as out, redirect_stdout(out):
            student.fonction()
            stu_ans = out.getvalue()
        with io.StringIO() as out, redirect_stdout(out):
            corr.fonction()
            corr_ans = out.getvalue()
        if(stu_ans == ''):  
            self.assertEqual(corr_ans, stu_ans, ansNoPrint)
        self.assertEqual(corr_ans, stu_ans, ans.format(stu_ans, corr_ans))       

if __name__ == '__main__':
    unittest.main()

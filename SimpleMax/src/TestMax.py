#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
from contextlib import redirect_stdout
import io
from inginious import feedback
import inginious_container_api.feedback as ingi_feedback

import CorrMax as corr
import max

tagDico = []

class TestMax(unittest.TestCase):

    
    
    
    
    
    def test_exists(self):
        #print("TAG:exist=True")
        if hasattr(max, 'afficheMax'):
            pass
            #print("TAG:exist=True")  # Tag indicating the function exists
            #print("TAG:overflow=True")  # Tag indicating the function exists
        else:
            #print("TAG:overflow=True")
            #print("TAG:exist=False")  # Tag indicating the function does not exist
            tagDico.append("overflow")
            tagDico.append("exist")
            tagTransfer()
        self.assertTrue(hasattr(max, 'afficheMax'), _("You have not defined the correct function. The function 'afficheMax' is missing."))

    def test_max(self):
        a = [random.randint(1, 100) for _ in range(25)]
        b = [random.randint(1, 100) for _ in range(25)]
        ans = _("The maximum of {} is {} and you have displayed {}.")
        ans2 = _("The maximum of {} is {} and you have displayed {}.\nThe function doesn't print anything. Remember to call the 'print()' function to display something.")
        all_tests_passed = True
        for i in range(len(a)):
            with io.StringIO() as out, redirect_stdout(out):
                max.afficheMax(a[i], b[i])
                stu_ans = out.getvalue()
            with io.StringIO() as out, redirect_stdout(out):
                corr.maximum(a[i], b[i])
                corr_ans = out.getvalue()
            if stu_ans == '':
                all_tests_passed = False
                self.assertEqual(corr_ans, stu_ans, ans2.format([a[i], b[i]], corr_ans, stu_ans))
            else:
                self.assertEqual(corr_ans, stu_ans, ans.format([a[i], b[i]], corr_ans, stu_ans))

        if all_tests_passed:
            print("TAG:max_correct=True")  # Tag indicating all max tests passed
        else:
            print("TAG:max_correct=False")  # Tag indicating some max tests failed
            
            
def tagTransfer():
    for tag in tagDico :
        print(f"TAG:{tag}=True")


if __name__ == '__main__':
    try:
        unittest.main()
    finally:
        tagTransfer()
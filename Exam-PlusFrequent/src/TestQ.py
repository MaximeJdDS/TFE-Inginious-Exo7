#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q
import Misconceptions

#tagDico=["MissnamingFunction"]
#if(hasattr(q, 'plus_frequent')):
tagDico = Misconceptions.runAllFunc(q.plus_frequent)
#Misconceptions.tagTransfer(tagDico)

class TestQ(unittest.TestCase):
    #def test_exist(self):
    #    Misconceptions.tagTransfer(tagDico)
    #    self.assertTrue(hasattr(q, 'plus_frequent'), ("Vous n'avez pas fourni la méthode demandée."))

    
    def test_one(self):
        feedback = _("Pour la liste {},\nla réponse attendue était {} et ta fonction a renvoyé {}.")
        Misconceptions.tagTransfer(tagDico)
        self.assertEqual(1, q.plus_frequent([1, 1, 2, 3]), feedback.format([1, 1, 2, 3],1,q.plus_frequent([1, 1, 2, 3])))


if __name__ == '__main__':
    unittest.main()

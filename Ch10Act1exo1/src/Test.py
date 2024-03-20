#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'viensIci')):
    tagDico = Misconceptions.runAllFunc(student.viensIci)
Misconceptions.tagTransfer(tagDico)

def tester_objet_attribut(objet):
    attributs_attendus = ['nom', 'race', 'x', 'y']
    

    for attribut in attributs_attendus:
        #self.assertTrue(hasattr(objet, attribut), _("Tu n\'as pas défini le bonne attribut. L'attribut {attribut} est introuvable."))
        
        if not hasattr(objet, attribut):
            return attribut
            print(f"L'objet n'a pas l'attribut {attribut}")
        #else:
            #print(f"L'objet a l'attribut {attribut}")
            
    return 0

            
def tester_objet_methode(objet):
    methodes_attendues = ['wouaf', 'viensIci']
    for methode in methodes_attendues:
        
        if not hasattr(objet, methode) or not callable(getattr(objet, methode)):
            return methode
            #self.assertTrue(False, _("Tu n\'as pas défini le bonne attribut. L'attribut {attribut} est introuvable."))
        #else:
            #print(f"L'objet a la méthode {methode}")
            
    return 0


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'Chien'), _("Tu n\'as pas defini la bonne Classe. La Classe 'Chien' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 69) for _ in range(5)]
        b = [random.randint(1, 69) for _ in range(5)]
        ansresult   = _("Pour la méthode viensIci({}) les attributs x,y n'ont pas été modifié correctement.")
        stu_obj = student.fonction("Médor","Teckel",0,0)
        corr_obj= corr.fonction("Médor","Teckel",0,0)
        test_attribut = tester_objet_attribut(stu_obj)
        test_meth = tester_objet_methode(stu_obj)
        if(test_attribut != 0):
            self.assertTrue(False, _("Tu n\'as pas défini le bonne attribut. L'attribut {} est introuvable.").format(test_attribut))
        if(test_meth != 0):
            self.assertTrue(False, _("Tu n\'as pas défini la bonne méthode. La méthode {} est introuvable.").format(test_meth))
        
        for i in range(len(a)):
            stu_obj.viensIci(a[i],b[i])
            corr_obj.viensIci(a[i],b[i])
            if(corr_obj.x != stu_obj.x): # x check
                self.assertEqual(corr_obj.x, stu_obj.x, ansresult.format([a[i],b[i]]))
            else: #y check
                self.assertEqual(corr_obj.y, stu_obj.y, ansresult.format([a[i],b[i]]))

    #def test_result_String(self):
     #   a = ["chat","chien","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","le"]
      #  ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
       # for i in range(len(a)):
        #    stu_ans  = student.fonction(a[i])
         #   corr_ans = corr.fonction(a[i])
          #  self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
from contextlib import redirect_stdout
import io

import Corr as corr
import student
from student import Pizza,Plat

def tester_objet_attribut(objet):
    attributs_attendus = ['typeDeFour']
    

    for attribut in attributs_attendus:
        #self.assertTrue(hasattr(objet, attribut), _("Tu n\'as pas défini le bonne attribut. L'attribut {attribut} est introuvable."))
        
        if not hasattr(objet, attribut):
            return attribut
            print(f"L'objet n'a pas l'attribut {attribut}")
        #else:
            #print(f"L'objet a l'attribut {attribut}")
            
    return 0

            
def tester_objet_methode(objet):
    methodes_attendues = ['__init__', 'surfacePizza']
    for methode in methodes_attendues:
        
        if not hasattr(objet, methode) or not callable(getattr(objet, methode)):
            return methode
            #self.assertTrue(False, _("Tu n\'as pas défini le bonne attribut. L'attribut {attribut} est introuvable."))
        #else:
            #print(f"L'objet a la méthode {methode}")
            
    return 0


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'Pizza'), _("Tu n\'as pas defini la bonne Classe. La Classe 'Pizza' est introuvable."))

    def test_result_Int(self):
        a = [random.randint(1, 69) for _ in range(10)]
        b = [random.randint(1, 569) for _ in range(10)]
        c = [random.randint(1, 1069) for _ in range(10)]
        d = [random.randint(1, 1069) for _ in range(10)]
        ansresult = _("Pour la méthode surfacePizza({}),\nLa réponse attendu était {}\nEt tu as renvoyé {}.")
        ansHerit  = _("Ta classe n'a pas hérité de la Classe Plat.")
        ansAdd    = _("L'addition de 2 objets Bourse ne fonctionne pas.\nBourse1 :{}\n+\nBourse2 :{}\nDoit donner :\n{}\nEt tu as renvoyé :\n{}")
        ansEchange= _("La méthode echange ne fonctionne pas. La bourse à échange :\n{}\n doit être réduite en :\n{}\nEt tu as renvoyé :\n{}.")
        #pizza(ingredient,prix,nom,isVege,typeDeFour)
        stu_obj = student.fonction(a[0],b[0],c[0],(c[0]%2)==0,d[0])
        corr_obj= corr.fonction(a[0],b[0],c[0],(c[0]%2)==0,d[0])
        rere =corr_obj.ingredient #####
        rere =stu_obj.ingredient
        self.assertEqual(True, issubclass(Pizza, Plat) , ansHerit.format())
        test_attribut = tester_objet_attribut(stu_obj)
        test_meth = tester_objet_methode(stu_obj)
        if(test_attribut != 0):
            self.assertTrue(False, _("Tu n\'as pas défini le bonne attribut. L'attribut {} est introuvable.").format(test_attribut))
        if(test_meth != 0):
            self.assertTrue(False, _("Tu n\'as pas défini la bonne méthode. La méthode {} est introuvable.").format(test_meth))
            
            
        #mid = int(/2)
        for i in range(len(a)): 
            corr_ans = corr_obj.surfacePizza(a[i])
            stu_ans  = stu_obj.surfacePizza(a[i])
            self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
            #stu_obj = student.fonction(a[i],b[i],c[i],(c[i]%2)==0,d[i])
            #corr_obj= corr.fonction(a[i],b[i],c[i],(c[i]%2)==0,d[i])
            #stu_obj2= student.fonction(a[i+mid],b[i+mid],c[i+mid],(c[i+mid]%2)==0,d[i+mid])
            #corr_obj2=corr.fonction(a[i+mid],b[i+mid],c[i+mid],(c[i+mid]%2)==0,d[i+mid])
            
            #self.assertEqual(str(corr_obj), str(stu_obj), ansStr.format(str(corr_obj),str(stu_obj)))# STR test
            
            
            #stu_obj3 = stu_obj + stu_obj2
            #corr_obj3 = corr_obj + corr_obj2
            #self.assertEqual(corr_obj3, stu_obj3, ansAdd.format(str(stu_obj),str(stu_obj2),str(corr_obj3),str(stu_obj3))) # ADD test
            
            
            #stu_obj3.echange()
            #corr_obj3.echange()
            #self.assertEqual(corr_obj3, stu_obj3, ansEchange.format(str(corr_obj + corr_obj2),str(corr_obj3),str(stu_obj3))) #Echange test
            
            

    #def test_result_String(self):
     #   a = ["chat","chien","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","le"]
      #  ansresult   = _("Pour le mot \"{}\" la réponse attendu est \"{}\" et ta fonction a renvoyé \"{}\".")
       # for i in range(len(a)):
        #    stu_ans  = student.fonction(a[i])
         #   corr_ans = corr.fonction(a[i])
          #  self.assertEqual(corr_ans, stu_ans, ansresult.format(a[i],corr_ans,stu_ans))
        
        
        #surface
        #
        #ECHANGE
        
       
    

if __name__ == '__main__':
    unittest.main()

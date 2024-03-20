#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import os
from unittest.mock import mock_open, patch

import Corr as corr
import student
import Misconceptions

tagDico=["MissnamingFunction"]
if(hasattr(student, 'ecritXfois')):
    tagDico = Misconceptions.runAllFunc(student.ecritXfois)
Misconceptions.tagTransfer(tagDico)


def compare2file(file1,file2):
    
    # reading files
    f1 = open(file1, "r") 
    f2 = open(file2, "r") 

    f1_data = f1.readlines()
    f2_data = f2.readlines()

    i = 0

    for line1 in f1_data:
        i += 1

        for line2 in f2_data:

            # matching line1 from both files
            if line1 == line2: 
            # print IDENTICAL if similar
                print("Line ", i, ": IDENTICAL")	 
            else:
                print("Line ", i, ":")
            # else print that line from both files
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
                f1.close()
                f2.close()
                return [i,line1,line2]
        break

    # closing files
    f1.close()
    f2.close() 
    return[-1,True,True]

def tester_fermeture_fichier(fonction_etudiant,argument):
    # Création d'un mock pour la fonction open
    with patch("builtins.open", mock_open()) as mock_file:
        # Appel de la fonction de l'étudiant
        fonction_etudiant(argument[0],argument[1],argument[2])

        # Vérification si le fichier est fermé
        mock_file.assert_called_once_with(argument[0], 'w')
        handle = mock_file()
        handle.close.assert_called_once()


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'ecritXfois'), _("Tu n\'as pas defini la bonne fonction. La fonction 'ecritXfois' est introuvable."))
    

    def test_result_String(self):
        fichierCorr = "resultCorrect.txt"
        fichierStu  = "resultStudent.txt"
        a = ["chat","chien","motsTresTresLongPourVoirSiLeSVaBienALaFinDuMot","le"]
        x = [random.randint(1, 10) for _ in range(len(a))]
        ansresult   = _("pour l'appel de ta fonction avec les arguments suivant: {} \nÀ la ligne \"{}\" \nla réponse attendu était \"{}\" \net ta fonction a renvoyé \"{}\".")
        noSuchFile  = _("Le fichier est introuvable, assure toi que tu écris dans le fichier dont le nom est donné en paramètre. ")
        for i in range(len(a)):
            if os.path.exists(fichierCorr):
                os.remove(fichierCorr)
            corr.fonction(fichierCorr,a[i],x[i])
            if os.path.exists(fichierStu):
                os.remove(fichierStu)
            student.fonction(fichierStu,a[i],x[i])
            
            if not(os.path.exists(fichierStu)):
                self.assertEqual(True,False, noSuchFile.format())
                
            tester_fermeture_fichier(student.ecritXfois,[fichierStu,a[i],x[i]])
            comparaisonBetween = compare2file(fichierCorr,fichierStu)
            self.assertEqual(comparaisonBetween[1], comparaisonBetween[2], ansresult.format(["fichier.txt",a[i],x[i]],comparaisonBetween[0],comparaisonBetween[1],comparaisonBetween[2]))
            if os.path.exists(fichierCorr):
                os.remove(fichierCorr)
            if os.path.exists(fichierStu):
                os.remove(fichierStu)


if __name__ == '__main__':
    unittest.main()

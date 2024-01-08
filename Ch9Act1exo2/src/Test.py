#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import os
from unittest.mock import mock_open, patch

import Corr as corr
import student


def listToFile(tab,filename):
    fic = open(filename,"w")
    for i in tab:
        fic.write(str(i)+"\n")
    fic.close()
    
def fileToStr(filename):
    result = ""
    fic = open(filename,"r")
    for line in fic:
        result = result + str(line)+"\n"
    fic.close()
    return result

def tester_fermeture_fichier(fonction_etudiant,argument):
    # Création d'un mock pour la fonction open
    with patch("builtins.open", mock_open()) as mock_file:
        # Appel de la fonction de l'étudiant
        fonction_etudiant(argument)

        # Vérification si le fichier est fermé
        mock_file.assert_called_once_with(argument, 'r')
        handle = mock_file()
        handle.close.assert_called_once()
        


class Test(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(student, 'fichierToList'), _("Tu n\'as pas defini la bonne fonction. La fonction 'fichierToList' est introuvable."))
    

    def test_result(self):
        fichierCorr = "resultCorrect.txt"
        fichierStu  = "resultStudent.txt"
        a = [random.randint(1,10000) for _ in range(random.randint(5,20))]
        
        ansresult   = _("Pour l'appel de ta fonction sur le fichier suivant : \n{} \nLa réponse attendu était \"{}\" \net ta fonction a renvoyé \"{}\".")
        
        for i in range(len(a)):
            if os.path.exists(fichierCorr):
                os.remove(fichierCorr)
            if os.path.exists(fichierStu):
                os.remove(fichierStu)
            content = [random.randint(1,10000) for _ in range(random.randint(5,20))]
            listToFile(content,fichierCorr)
            listToFile(content,fichierStu)
            
            ansCorr = corr.fonction(fichierCorr)
            
            ansStu = student.fonction(fichierStu)
                            
            tester_fermeture_fichier(student.fichierToList,fichierStu)
            
            fileStr = fileToStr(fichierStu)
            
            if os.path.exists(fichierCorr):
                os.remove(fichierCorr)
            if os.path.exists(fichierStu):
                os.remove(fichierStu)
                
            self.assertEqual(ansCorr, ansStu, ansresult.format(fileStr,ansCorr,ansStu))
            
            


if __name__ == '__main__':
    unittest.main()

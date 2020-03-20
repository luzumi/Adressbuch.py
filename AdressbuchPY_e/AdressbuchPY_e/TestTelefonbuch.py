"""modul zu Testen der einzelnen Funktionen"""

import unittest
from Telefonbuch import *

class TestTelefonbuch(unittest.TestCase):       #erbt con unittest.Testcase
    """description of class"""

    def setUp(self):        #wird vor jedem Test aufgerufen
        self.testObj = Telefonbuch() 
  
    def testAddnummer(self):
        self.testObj.addNummer("Daniel","Neubieser","0172/4283230")
        self.assertEqual(self.testObj.getNummer("Daniel","Neubieser"),"0172/4283230")
       
    #def testDeleteNummer(self):
        liste = []
    # #   self.assertEqual(self.testObj.getNummer("Daniel","Neubieser"),[0],"0172/4283230")
        #Telfonnummer löschen
    #    self.testObj.deleteNummer("0172/4283230")
    #  #  self.assertEqual(self.testObj.getNummer("Daniel","Neubieser"),liste)

if __name__ == "__main__":  #Python-Convention, startet die eigentliche main (hier aber unittest.main)
    unittest.main()


    
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alkutiedot_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_kateisostot_toimii(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(takaisin,160)
        takaisin = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(takaisin,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset,1)
        
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(560)
        self.assertEqual(takaisin,160)
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(takaisin,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_korttiostot_toimii(self):
        kortti = Maksukortti(700)

        tosi = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tosi,True)
        tosi = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tosi,True)
        
        epatosi = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(epatosi,False)
        epatosi = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(epatosi,False)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(str(kortti), "saldo: 0.6")
    
    def test_rahan_lataus_toimii(self):
        kortti = Maksukortti(100)

        self.kassapaate.lataa_rahaa_kortille(kortti,-20)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(str(kortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.rikaskortti = Maksukortti(10000)
        self.koyhakortti = Maksukortti(10)
    
    #Alkutilanne
    def test_rahamaara_on_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisten_maara_on_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)    

    def test_maukkaiden_maara_on_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Käteisostot
    def test_kassa_kasvaa_oikein_kun_maksu_on_riittava_edulliset_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kassa_kasvaa_oikein_kun_maksu_on_riittava_maukkaat_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtorahan_suuruus_on_oikea_kun_maksu_on_riittava_edulliset_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_vaihtorahan_suuruus_on_oikea_kun_maksu_on_riittava_maukkaat_kateinen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_myytyjen_lounaiden_maara_kasvaa_kun_maksu_on_riittava_edulliset_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_myytyjen_lounaiden_maara_kasvaa_kun_maksu_on_riittava_maukkaat_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassa_ei_kasva_kun_maksu_ei_ole_riittava_edulliset_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_ei_kasva_kun_maksu_ei_ole_riittava_maukkaat_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahat_palautetaan_kun_maksu_ei_ole_riittava_edulliset_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(50), 50)

    def test_rahat_palautetaan_kun_maksu_ei_ole_riittava_maukkaat_kateinen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(50), 50)

    def test_myytyjen_lounaiden_maara_ei_kasva_kun_maksu_ei_ole_riittava_edulliset_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_lounaiden_maara_ei_kasva_kun_maksu_ei_ole_riittava_maukkaat_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #Korttiostot
    def test_summa_veloitetaan_kortilta_jos_on_tarpeeksi_rahaa_edulliset(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.rikaskortti))

    def test_summa_veloitetaan_kortilta_jos_on_tarpeeksi_rahaa_maukkaat(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.rikaskortti))  

    def test_summaa_ei_veloiteta_kortilta_jos_ei_ole_tarpeeksi_rahaa_edulliset(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti))

    def test_summaa_ei_veloiteta_kortilta_jos_ei_ole_tarpeeksi_rahaa_maukkaat(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti))

    def test_myytyjen_lounaiden_maara_kasvaa_kun_maksu_on_riittava_edulliset_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rikaskortti)
        self.kassapaate.syo_edullisesti_kortilla(self.rikaskortti)
        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_myytyjen_lounaiden_maara_kasvaa_kun_maksu_on_riittava_maukkaat_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rikaskortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myytyjen_lounaiden_maara_ei_kasva_kun_maksu_on_riittava_edulliset_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_lounaiden_maara_ei_kasva_kun_maksu_on_riittava_maukkaat_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def kassassa_oleva_raha_ei_muutu_kortilla_maksaessa_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rikaskortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def kassassa_oleva_raha_ei_muutu_kortilla_maksaessa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rikaskortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_muuttuu_rahaa_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.rikaskortti, 100)
        self.assertEqual(self.rikaskortti.saldo, 10100)

    def test_kassan_saldo_muuttuu_rahaa_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.rikaskortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kassan_saldo_ei_muuta_kun_ladataan_negatiivista_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.rikaskortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

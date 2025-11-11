import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_Luodun_kassapäätteen_rahamäärä_ja_myytyjen_lounaiden_määrä_on_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_Käteisosto_toimii_edullisten_osalta(self):
        takas = self.kassa.syo_edullisesti_kateisella(1000)
        self.assertEqual(takas, 760)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_Käteisosto_toimii_maukkaiden_osalta(self):
        takas = self.kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual(takas, 600)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_ei_toimi_edullisten_osalta(self):
        takas = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(takas, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_Käteisosto_ei_toimi_maukkaiden_osalta(self):
        takas = self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(takas, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_Korttiosto_toimii_edullisten_osalta_true(self):
        visa = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(visa)
        self.assertEqual(self.kortti.saldo, 760)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_Korttiosto_toimii_maukkaiden_osalta_true(self):
        visa = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(visa)
        self.assertEqual(self.kortti.saldo, 600)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_Korttiosto_ei_toimi_edullisten_osalta_false(self):
        palikka = Maksukortti(0)
        visa = self.kassa.syo_edullisesti_kortilla(palikka)
        self.assertFalse(visa)
        self.assertEqual(palikka.saldo, 0)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_Korttiosto_ei_toimii_maukkaiden_osalta_false(self):
        palikka = Maksukortti(0)
        visa = self.kassa.syo_maukkaasti_kortilla(palikka)
        self.assertFalse(visa)
        self.assertEqual(palikka.saldo, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_Kassassa_oleva_rahamäärä_ei_muutu_kortilla_ostettaessa(self):
        visa = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(visa)
        self.assertEqual(self.kortti.saldo, 760)
        self.assertEqual(self.kassa.edulliset, 1)

        visa = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(visa)
        self.assertEqual(self.kortti.saldo, 360)
        self.assertEqual(self.kassa.maukkaat, 1)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_Kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamäärä_kasvaa_ladatulla_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 2000)

        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_Kortille_neg_rahaa_ladattaessa_kortin_ei_saldo_muuttuu_ja_kassassa_oleva_rahamäärä_pysyy(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kortti.saldo, 1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 100000/100)
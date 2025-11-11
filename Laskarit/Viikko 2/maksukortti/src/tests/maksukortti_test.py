import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        kortti = Maksukortti(1000)
        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(1000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 9.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        # varmistetaan että saldoa jäljellä 7.5 euroa eli 750 senttiä
        self.assertEqual(kortti.saldo, 750)

    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

import unittest
from pelilauta import PeliLauta

class TestPeliLauta(unittest.TestCase):
    def setUp(self):
        self.peli = PeliLauta()
        self.peli.uusi_peli()

    def test_sallittu_siirto_kun_sarakkeessa_tilaa(self):
        self.assertEqual(self.peli.sallittu_siirto(0), True)
        self.assertEqual(self.peli.sallittu_siirto(1), True)
        self.peli.lauta[1][2] = 1
        self.assertEqual(self.peli.sallittu_siirto(2), True)

    def test_sallittu_siirto_hyl_kun_sarake_taynna(self):
        self.peli.lauta[0][3] = 1
        self.peli.lauta[0][4] = 2
        self.assertEqual(self.peli.sallittu_siirto(3), False)
        self.assertEqual(self.peli.sallittu_siirto(4), False)

    def test_sallittu_siirto_vaaralla_syotteella(self):
        self.assertEqual(self.peli.sallittu_siirto(-3), False)
        self.assertEqual(self.peli.sallittu_siirto("a"), False)
        self.assertEqual(self.peli.sallittu_siirto(9), False)

    def test_tarkista_voitto_rivi(self):
        self.peli.lauta[0][2] = 1
        self.peli.lauta[0][3] = 1
        self.peli.lauta[0][4] = 1
        self.peli.lauta[0][5] = 1
        self.peli.viimeisin_siirto = (0,5)
        self.assertEqual(self.peli.tarkista_voitto(), True)

    def test_tarkista_voitto_pysty(self):
        self.peli.lauta[0][2] = 2
        self.peli.lauta[1][2] = 2
        self.peli.lauta[2][2] = 2
        self.peli.lauta[3][2] = 2
        self.peli.viimeisin_siirto = (0,2)
        self.assertEqual(self.peli.tarkista_voitto(), True)

    def test_tarkista_voitto_viisto_1(self):
        self.peli.lauta[5][2] = 1
        self.peli.lauta[4][3] = 1
        self.peli.lauta[3][4] = 1
        self.peli.lauta[2][5] = 1
        self.peli.viimeisin_siirto = (2,5)
        self.assertEqual(self.peli.tarkista_voitto(), True)

    def test_tarkista_voitto_viisto_2(self):
        self.peli.lauta[1][0] = 1
        self.peli.lauta[2][1] = 1
        self.peli.lauta[3][2] = 1
        self.peli.lauta[4][3] = 1
        self.peli.viimeisin_siirto = (1,0)
        self.assertEqual(self.peli.tarkista_voitto(), True)

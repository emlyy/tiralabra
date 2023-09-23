import unittest
import numpy as np
from pelilauta import PeliLauta
from toiminnot import *

class TestToiminnot(unittest.TestCase):
    def setUp(self):
        self.peli = PeliLauta()
        self.peli.uusi_peli()
        self.lauta = self.peli.lauta

    def test_sallittu_siirto_kun_sarakkeessa_tilaa(self):
        self.assertEqual(sallittu_siirto(self.lauta, 0), True)
        self.assertEqual(sallittu_siirto(self.lauta, 1), True)
        self.lauta[1][2] = 1
        self.assertEqual(sallittu_siirto(self.lauta, 2), True)

    def test_sallittu_siirto_hyl_kun_sarake_taynna(self):
        self.lauta[0][3] = 1
        self.lauta[0][4] = 2
        self.assertEqual(sallittu_siirto(self.lauta, 3), False)
        self.assertEqual(sallittu_siirto(self.lauta, 4), False)

    def test_sallittu_siirto_vaaralla_syotteella(self):
        self.assertEqual(sallittu_siirto(self.lauta, -3), False)
        self.assertEqual(sallittu_siirto(self.lauta, "a"), False)
        self.assertEqual(sallittu_siirto(self.lauta, 9), False)

    def test_tarkista_voitto_rivi(self):
        self.lauta[0][2] = 1
        self.lauta[0][3] = 1
        self.lauta[0][4] = 1
        self.lauta[0][5] = 1
        self.assertEqual(tarkista_voitto(self.lauta, (0,5)), True)

    def test_tarkista_voitto_pysty(self):
        self.lauta[0][2] = 2
        self.lauta[1][2] = 2
        self.lauta[2][2] = 2
        self.lauta[3][2] = 2
        self.assertEqual(tarkista_voitto(self.lauta, (0,2)), True)

    def test_tarkista_voitto_viisto_1(self):
        self.lauta[5][2] = 1
        self.lauta[4][3] = 1
        self.lauta[3][4] = 1
        self.lauta[2][5] = 1
        self.assertEqual(tarkista_voitto(self.lauta, (2,5)), True)

    def test_tarkista_voitto_viisto_2(self):
        self.lauta[1][0] = 1
        self.lauta[2][1] = 1
        self.lauta[3][2] = 1
        self.lauta[4][3] = 1
        self.assertEqual(tarkista_voitto(self.lauta, (1,0)), True)

    def test_vapaa_rivi(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 2, 2, 2, 1]])
        self.assertEqual(vapaa_rivi(lauta, 3), 3)
        self.assertEqual(vapaa_rivi(lauta, 1), 5)
        self.assertEqual(vapaa_rivi(lauta, 5), 4)

    def test_taynna(self):
        lauta = np.ones((RIVIT,SARAKKEET), dtype=int)
        self.assertEqual(taynna(lauta), True)

    def test_taynna_kun_tilaa(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 1, 1, 0, 0],
                          [0, 0, 1, 2, 2, 2, 1]])
        self.assertEqual(taynna(lauta), False)
        self.assertEqual(taynna(self.lauta), False)

    def test_siirra(self):
        siirra(self.lauta, 3, 5, 2)
        self.assertEqual(self.lauta[3][5], 2)

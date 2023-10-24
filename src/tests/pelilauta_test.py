import unittest
from config import RIVIT, SARAKKEET
from pelilauta import PeliLauta

class TestPeliLauta(unittest.TestCase):
    def setUp(self):
        self.peli = PeliLauta()
        self.peli.uusi_peli()

    def test_uusi_peli(self):
        self.peli.lauta = 0
        self.peli.uusi_peli()
        list_1 = self.peli.lauta
        list_2 = ([[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]])
        self.assertListEqual(list_1, list_2) 

    def test_paivittaa_viimeisen_siirron(self):
        self.peli.paivita_lauta(3, 4, 1)
        self.assertEqual(self.peli.lauta[3][4], 1)

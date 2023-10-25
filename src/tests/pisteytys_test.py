import unittest
from tekoaly.pisteytys import tarkista_varma_kolme, pisteytys_vaaka, pisteytys_pysty, pisteytys_nouseva_viisto, pisteytys_laskeva_viisto

class TestPisteytys(unittest.TestCase):
    def setUp(self):
        self.arvo = 0
        self.syvyys = 5

    def test_varma_kolmen_suora(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [2, 2, 2, 1, 2, 1, 0]])
        self.arvo = tarkista_varma_kolme(lauta, 2, self.syvyys)
        self.assertEqual(self.arvo, -500000*(self.syvyys+1))

    def test_varma_kolmen_suora_alin_rivi(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 2, 2, 2, 0]])
        self.arvo = tarkista_varma_kolme(lauta, 2, self.syvyys)
        self.assertEqual(self.arvo, 500000*(self.syvyys+1))

    def test_varma_kolmen_suora_ei(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0],
                [0, 2, 0, 2, 1, 2, 0]])
        self.arvo = tarkista_varma_kolme(lauta, 1, self.syvyys)
        self.assertEqual(self.arvo, 0)

    def test_kolmen_suora_vaaka(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0],
                [0, 0, 1, 2, 2, 2, 0]])
        self.arvo = pisteytys_vaaka(lauta, 2)
        self.assertEqual(self.arvo, 10000)

    def test_ei_kolmen_suora_vaaka(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0],
                [0, 0, 1, 2, 2, 2, 1]])
        self.arvo = pisteytys_vaaka(lauta, 2)
        self.assertEqual(self.arvo, 0)

    def test_kolmen_suora_pysty(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0],
                [0, 0, 2, 1, 1, 0, 0],
                [0, 0, 1, 2, 2, 0, 0]])
        self.arvo = pisteytys_pysty(lauta, 2)
        self.assertEqual(self.arvo, -9000)

    def test_ei_kolmen_suora_pysty(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 2, 0, 0],
                [0, 0, 2, 1, 1, 0, 0],
                [0, 0, 1, 2, 0, 0, 0]])
        self.arvo = pisteytys_pysty(lauta, 1)
        self.assertEqual(self.arvo, 0)

    def test_kolmen_suora_viisto_1(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 2, 0, 0],
                [0, 0, 1, 2, 2, 0, 0]])
        self.arvo = pisteytys_nouseva_viisto(lauta, 2)
        self.assertEqual(self.arvo, -9000)

    def test_kolmen_suora_viisto_2(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 1, 2, 1, 0],
                [0, 0, 1, 2, 1, 2, 0]])
        self.arvo = pisteytys_laskeva_viisto(lauta, 2)
        self.assertEqual(self.arvo, 10000)

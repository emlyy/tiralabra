import unittest
import numpy as np
from tekoaly.pisteytys import tarkista_varma_kolme, pisteytys_vaaka, pisteytys_pysty, pisteytys_nouseva_viisto, pisteytys_laskeva_viisto

class TestPisteytys(unittest.TestCase):
    def setUp(self):
        self.arvo = 0

    def test_varma_kolmen_suora(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 1, 1, 0, 0],
                          [2, 2, 2, 1, 2, 1, 0]])
        self.arvo = tarkista_varma_kolme(lauta, 2)
        self.assertEqual(self.arvo, -500000)

    def test_varma_kolmen_suora_alin_rivi(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 2, 2, 2, 0]])
        self.arvo = tarkista_varma_kolme(lauta, 2)
        self.assertEqual(self.arvo, 500000)

    def test_varma_kolmen_suora_ei(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 0],
                          [0, 2, 0, 2, 1, 2, 0]])
        self.arvo = tarkista_varma_kolme(lauta, 1)
        self.assertEqual(self.arvo, 0)

    def test_kolmen_suora_vaaka(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 2, 2, 2, 0]])
        self.arvo = pisteytys_vaaka(lauta, 2)
        self.assertEqual(self.arvo, 10000)

    def test_ei_kolmen_suora_vaaka(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 2, 2, 2, 1]])
        self.arvo = pisteytys_vaaka(lauta, 2)
        self.assertEqual(self.arvo, 0)

    def test_kolmen_suora_pysty(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 1, 2, 0, 0],
                          [0, 0, 2, 1, 1, 0, 0],
                          [0, 0, 1, 2, 2, 0, 0]])
        self.arvo = pisteytys_pysty(lauta, 2)
        self.assertEqual(self.arvo, -9000)

    def test_ei_kolmen_suora_pysty(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 2, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 1, 1, 2, 0, 0],
                          [0, 0, 2, 1, 1, 0, 0],
                          [0, 0, 1, 2, 0, 0, 0]])
        self.arvo = pisteytys_pysty(lauta, 1)
        self.assertEqual(self.arvo, 0)

    def test_kolmen_suora_viisto_1(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 2, 0, 0],
                          [0, 0, 1, 2, 2, 0, 0]])
        self.arvo = pisteytys_nouseva_viisto(lauta, 2)
        self.assertEqual(self.arvo, -9000)

    def test_kolmen_suora_viisto_2(self):
        lauta = np.array([[0, 0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 2, 0, 0, 0],
                          [0, 0, 0, 1, 2, 1, 0],
                          [0, 0, 1, 2, 1, 2, 0]])
        self.arvo = pisteytys_laskeva_viisto(lauta, 2)
        self.assertEqual(self.arvo, 10000)

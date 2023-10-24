import unittest
import numpy as np
from tekoaly.minimax import paras_siirto

class TestParasSiirto(unittest.TestCase):
    def setUp(self):
        pass

    def test_estaa_neljan_pysty(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0],
                [0, 0, 0, 2, 1, 0, 0],
                [0, 0, 2, 1, 2, 0, 0]])
        self.siirto = paras_siirto(lauta, 33)
        self.assertEqual(self.siirto, 3)

    def test_estaa_neljan_vaaka(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0],
                [0, 0, 0, 2, 1, 0, 0],
                [0, 0, 2, 1, 1, 1, 0]])
        self.siirto = paras_siirto(lauta, 33)
        self.assertEqual(self.siirto, 6)

    def test_estaa_neljan_viisto_1(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [0, 0, 2, 1, 0, 0, 0],
                [0, 0, 1, 2, 1, 0, 0],
                [0, 0, 2, 1, 2, 0, 0]])
        self.siirto = paras_siirto(lauta, 33)
        self.assertEqual(self.siirto, 5)

    def test_estaa_neljan_viisto_2(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 1, 1, 1],
                [0, 0, 0, 2, 1, 2, 2],
                [0, 0, 1, 1, 2, 2, 1]])
        self.siirto = paras_siirto(lauta, 29)
        self.assertEqual(self.siirto, 6)

    def test_voitto_pysty(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 1, 1, 0],
                [0, 0, 1, 1, 2, 1, 0]])
        self.siirto = paras_siirto(lauta, 33)
        self.assertEqual(self.siirto, 3)

    def test_voitto_vaaka(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 1, 1, 2, 0],
                [0, 0, 2, 2, 2, 1, 0]])
        self.siirto = paras_siirto(lauta, 33)
        self.assertEqual(self.siirto, 1)

    def test_voitto_viisto_1(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 2, 0, 0, 0, 0],
                [0, 2, 1, 0, 0, 0, 0],
                [0, 1, 2, 1, 0, 0, 0],
                [0, 2, 1, 2, 0, 0, 0],
                [1, 1, 2, 1, 0, 0, 0]])
        self.siirto = paras_siirto(lauta, 29)
        self.assertEqual(self.siirto, 4)

    def test_voitto_viisto_2(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 0, 1, 2, 1],
                [0, 0, 0, 0, 2, 1, 2],
                [0, 0, 0, 2, 1, 1, 1]])
        self.siirto = paras_siirto(lauta, 31)
        self.assertEqual(self.siirto, 6)

    def test_molemmilla_kolme(self):
        lauta = ([[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0],
                [0, 0, 0, np.array1, 2, 0, 0],
                [0, 0, 0, 1, 2, 0, 0]])
        self.siirto = paras_siirto(lauta, 36)
        self.assertEqual(self.siirto, 4)
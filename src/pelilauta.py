import numpy as np
from toiminnot import siirra
from config import RIVIT, SARAKKEET

class PeliLauta:
    """Luokka vastaa pelilaudan päivityksestä.

    Attributes:
        rivit: rivien lkm pelilaudalla
        sarakkeet: sarakkeiden lkm pelilaudalla
        lauta: Pelilaudan tilannetta kuvaava matriisi. Aluksi kaikki
            tilat tyhjiä eli 0. 1: pelaaja. 2: tekoäly.
        viimeisin_siirto: tuple, (x,y) missä x rivi ja y sarake.
    """
    def __init__(self):
        self.lauta = None
        self.viimeisin_siirto = None

    def __str__(self):
        """Palauttaa pelin tulostettavassa muodossa.

        Returns:
            str: otsikko Connect Four ja pelilauta
        """
        return f"Connect Four \n {self.lauta}"

    def uusi_peli(self):
        """Luo uuden pelilaudan.
        """
        self.lauta = np.zeros((RIVIT,SARAKKEET), dtype=int)

    def paivita_lauta(self, rivi, sarake, pelaaja):
        """Päivittää siirron matriisiin. Tallentaa viimeisimmän siirron muuttujaan.

        Args:
            rivi (int): Valittu rivi.
            sarake (int): Valittu sarake.
            pelaaja (int): 1: pelaaja. 2: tekoäly.
        """
        siirra(self.lauta, rivi, sarake, pelaaja)
        self.viimeisin_siirto = (rivi, sarake)

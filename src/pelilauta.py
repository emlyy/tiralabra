import numpy as np

class PeliLauta:
    """Luokka vastaa pelilaudan päivityksestä.

    Attributes:
        rivit: rivien lkm pelilaudalla
        sarakkeet: sarakkeiden lkm pelilaudalla
        lauta: Pelilaudan tilannetta kuvaava matriisi. Aluksi kaikki tilat tyhjiä eli 0. 1: pelaaja. 2: tekoäly.
        viimeisin_siirto: tuple, (x,y) missä x rivi ja y sarake.
    """
    def __init__(self):
        self.rivit = 6
        self.sarakkeet = 7
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
        self.lauta = np.zeros((6,7), dtype=int)

    def paivita_lauta(self, rivi, sarake, pelaaja):
        """Päivittää siirron matriisiin. Tallentaa viimeisimmän siirron muuttujaan.

        Args:
            rivi (int): Valittu rivi.
            sarake (int): Valittu sarake.
            pelaaja (int): 1: pelaaja. 2: tekoäly.
        """
        self.lauta[rivi][sarake] = pelaaja
        self.viimeisin_siirto = (rivi, sarake)

    def sallittu_siirto(self, sarake):
        """Tarkistaa, onko pelilaudalla valitussa sarakkeessa tilaa.

        Args:
            sarake (int): Valittu sarake.

        Returns:
            boolean: Palauttaa True, jos sarakkeessa on vielä tilaa. False jos sarake täynnä tai ei kuulu laudalle.
        """
        if sarake in range(self.sarakkeet):
            return self.lauta[0][sarake] == 0
        return False

    def vapaa_rivi(self, sarake):
        """Tarkistaa mihin seuraava pala tiputetaan.

        Args:
            sarake (int): Valittu sarake.

        Returns:
            int: Palauttaa sarakkeessa alimman vapaana olevan rivin, mihin pala tippuu.
        """
        for rivi in range(self.rivit-1,-1,-1):
            if self.lauta[rivi][sarake] == 0:
                return rivi

    def taynna(self):
        """Tarkistaa onko pelilauta täynnä.

        Returns:
            boolean: Palauttaa False niin kauan, kun lauta ei ole täynnä.
        """
        for sarake in range(self.sarakkeet):
            if self.lauta[0][sarake] == 0:
                return False
        return True

    def tarkista_voitto(self):
        """Tarkistaa onko toinen pelaajista saanut neljän suoran.

        Returns:
            boolean: Palauttaa True, jos löytyy neljän suora, muuten palauttaa False.
        """
        for sarake in range(self.sarakkeet-3):
            if self.lauta[self.viimeisin_siirto[0]][sarake] == self.lauta[self.viimeisin_siirto[0]][sarake+1] == self.lauta[self.viimeisin_siirto[0]][sarake+2] == self.lauta[self.viimeisin_siirto[0]][sarake+3] != 0:
                return True
        for rivi in range(self.rivit-3):
            if self.lauta[rivi][self.viimeisin_siirto[1]] == self.lauta[rivi+1][self.viimeisin_siirto[1]] == self.lauta[rivi+2][self.viimeisin_siirto[1]] == self.lauta[rivi+3][self.viimeisin_siirto[1]] != 0:
                return True
        for rivi in range (self.rivit-3):
            for sarake in range(self.sarakkeet-3):
                if self.lauta[rivi][sarake] == self.lauta[rivi+1][sarake+1] == self.lauta[rivi+2][sarake+2] == self.lauta[rivi+3][sarake+3] != 0:
                    return True
        for rivi in range (3,self.rivit):
            for sarake in range(self.sarakkeet-3):
                if self.lauta[rivi][sarake] == self.lauta[rivi-1][sarake+1] == self.lauta[rivi-2][sarake+2] == self.lauta[rivi-3][sarake+3] != 0:
                    return True
        return False

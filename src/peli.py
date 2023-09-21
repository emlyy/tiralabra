from random import randint
from pelilauta import PeliLauta
from toiminnot import *

class Peli:
    """Luokka vastaa pelin silmukasta.
    """
    def __init__(self) -> None:
        self.peli = PeliLauta()

    def siirto(self, sarake, pelaaja):
        """Kutsuu tarvittavat funktiot siirtoa varten.

        Args:
            sarake (int): Valittu sarake.
            pelaaja (int): 1: pelaaja, 2: tekoäly

        Returns:
            boolean: Palauttaa false jos siirto ei onnistunut.
        """
        lauta = self.peli.lauta
        if sallittu_siirto(lauta, sarake):
            rivi = vapaa_rivi(lauta, sarake)
            self.peli.paivita_lauta(rivi, sarake, pelaaja)
            return True
        return False

    def silmukka(self):
        """Pelin silmukka. Kysyy pelaajan siirtoa, kutsuu päivittävät funktiot, tulostaa pelilaudan.
        """
        self.peli.uusi_peli()
        vuoro = 0
        kaynnissa = True
        tasapeli = False
        print(self.peli)
        while kaynnissa:
            if vuoro % 2 == 0:
                sarake = int(input("Valitse sarake (0-6): "))
                if not self.siirto(sarake, 1):
                    print("Valinta ei ole mahdollinen.")
                    continue
            else:
                sarake = randint(0,6)
                if not self.siirto(sarake, 2):
                    continue
            if tarkista_voitto(self.peli.lauta, self.peli.viimeisin_siirto):
                kaynnissa = False
            if taynna(self.peli.lauta):
                tasapeli = True
                kaynnissa = False
            vuoro += 1
            print(self.peli)
        if tasapeli:
            print("Tasapeli!")
        else:
            if vuoro % 2 == 0:
                print("Hävisit! :(")
            else:
                print("Voitit pelin! :D")

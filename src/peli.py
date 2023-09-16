from random import randint
from pelilauta import PeliLauta

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
        if self.peli.sallittu_siirto(sarake):
            rivi = self.peli.vapaa_rivi(sarake)
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
            if self.peli.tarkista_voitto():
                kaynnissa = False
            if self.peli.taynna():
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

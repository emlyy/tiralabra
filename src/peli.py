from pelilauta import PeliLauta
from random import randint

class Peli:
    """Luokka vastaa pelin silmukasta.
    """
    def __init__(self) -> None:
        self.peli = PeliLauta()

    def siirto(self, sarake, pelaaja):
        if self.peli.sallittu_siirto(sarake):
                rivi = self.peli.vapaa_rivi(sarake)
                self.peli.paivita_lauta(rivi, sarake, pelaaja)
                return True
        return False

    def silmukka(self):
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

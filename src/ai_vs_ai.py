import pygame
import numpy as np
from copy import deepcopy
from pelilauta import PeliLauta
from tekoaly.minimax import minimax
from toiminnot import tarkista_voitto, sallittu_siirto, vapaa_rivi
from kayttoliittyma import Kayttoliittyma
from config import (RIVIT, SARAKKEET, NAYTON_KOKO, FONT, TEKSTI_1_PAIKKA,
    TEKSTI_2_PAIKKA, SININEN, TUMMAN_SININEN, SYVYYS_KELT, SYVYYS_PUN, KELTAINEN,
    PUNAINEN, MUSTA, HARMAA, TEKSTI_3_PAIKKA, LAUTA_X, LAUTA_Y, LEVEYS, KORKEUS, REUNA, HALKASIJA, LISA_X)

class Tekoaly_Peli:
    """Käyttöliittymä tekoäly vastaan tekoäly pelille.
    """
    def __init__(self):
        pygame.init()
        self.peli = PeliLauta()
        self.naytto = pygame.display.set_mode(NAYTON_KOKO)
        self.kello = pygame.time.Clock()
        self.kaynnissa = True
        self.tasapeli = False
        self.resetointi = False
        self.vuoro = 42
        self.ohje_teksti = "keltainen aloittaa"
        self.teksti_vari = MUSTA
        self.font = pygame.font.SysFont(FONT, 40)
        pygame.display.set_caption("Connect Four")

    def siirto(self, sarake: int, pelaaja: int):
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

    def lopetus_naytto(self):
        """Silmukka, joka suorittaa lopetus näytön.

        Piirtää näytön ja tarkistaa pelaajan syötteitä uudelleen aloittamisen varalta.
        """
        while True:
            self.tapahtumat()
            if self.resetointi:
                self.aloita_alusta()
                self.peli_silmukka()
                break
            if self.tasapeli:
                self.ohje_teksti = "Tasapeli!"
            else:
                if self.vuoro % 2 == 0:
                    self.ohje_teksti = "Punainen voittaa"
                    self.teksti_vari = PUNAINEN
                else:
                    self.ohje_teksti = "Keltainen voittaa"
                    self.teksti_vari = KELTAINEN
            self.piirra_naytto()

    def peli_silmukka(self):
        """Pelin silmukka. Käy läpi tapahtumat, päivittää ja tulostaa näytön.
        Valitsee vuorotellen parhaan siirron.
        """
        self.peli.uusi_peli()
        self.piirra_naytto()
        while self.kaynnissa:
            pelaaja = 2
            syvyys = SYVYYS_PUN
            if self.vuoro % 2 == 0:
                pelaaja = 1
                syvyys = SYVYYS_KELT
            self.tapahtumat()
            if syvyys <= 9:
                pygame.time.wait(2000)
            sarake = self.paras_siirto(self.peli.lauta, self.vuoro, syvyys)
            if not self.siirto(sarake, pelaaja):
                self.ohje_teksti = "ongelma"
                continue
            self.ohje_teksti = "keltaisen vuoro"
            self.paivita()
            self.piirra_naytto()
        self.lopetus_naytto()

    def tapahtumat(self):
        """Käy läpi pelaajan syötteet.
        """
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                self.kaynnissa = False
                pygame.quit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE:
                    self.resetointi = True

    def aloita_alusta(self):
        """Aloittaa pelin alusta.
        """
        self.resetointi = False
        self.kaynnissa = True
        self.tasapeli = False
        self.vuoro = 42
        self.peli.uusi_peli()
        self.ohje_teksti = "uusi peli"

    def piirra_naytto(self):
        """Piirtää laudan ja tekstit.
        """
        self.naytto.fill(HARMAA)
        self.piirra_pelilauta()
        teksti_1 = self.font.render("Tervetuloa!", True, MUSTA)
        self.naytto.blit(teksti_1, (TEKSTI_1_PAIKKA))
        teksti_2 = self.font.render(self.ohje_teksti, True, self.teksti_vari)
        self.naytto.blit(teksti_2, (TEKSTI_2_PAIKKA))
        teksti_3 = self.font.render("Aloita peli alusta painamalla ESC.", True, MUSTA)
        self.naytto.blit(teksti_3, (TEKSTI_3_PAIKKA))
        pygame.display.update()
        self.kello.tick(30)

    def piirra_pelilauta(self):
        """Vastaa pelilaudan piirtämisestä.
        """
        pygame.draw.rect(self.naytto, SININEN, pygame.Rect(LAUTA_X, LAUTA_Y, LEVEYS, KORKEUS))
        for rivi in range(RIVIT):
            for sarake in range(SARAKKEET):
                if self.peli.lauta[rivi][sarake] == 1:
                    väri = KELTAINEN
                elif self.peli.lauta[rivi][sarake] == 2:
                    väri = PUNAINEN
                else:
                    väri = TUMMAN_SININEN
                pygame.draw.circle(self.naytto, väri, (LISA_X+(HALKASIJA+2)*(sarake+1), REUNA+(HALKASIJA+2)*(rivi+1)),HALKASIJA/2)

    def paivita(self):
        """Tarkistaa voiton ja tasapelin. Päivittää vuoron.
        """
        if tarkista_voitto(self.peli.lauta, self.peli.viimeisin_siirto):
            self.kaynnissa = False
        if self.vuoro == 1 and self.kaynnissa:
            self.tasapeli = True
            self.kaynnissa = False
        self.vuoro -= 1
        if self.vuoro % 2 != 0:
            self.ohje_teksti = "Punaisen vuoro"
    
    def paras_siirto(self, lauta, siirtojen_maara: int, syvyys):
        """Kokeilee siirtovaihtoehdot keskeltä ulospäin käyttäen minimax algoritmia ja
        valitsee parhaan siirron.

        Args:
        lauta (_type_): Pelilaudan tämänhetkinen tilanne.
        siirtojen_maara (int): Kertoo kuinka monta siirtoa on jäljellä tasapeliin.
        syvyys (int): syvyys mikä halutaan käydä läpi minimaxilla

        Returns:
        int: Palauttaa valitun sarakkeen.
        """
        kopio_lauta = deepcopy(lauta)
        if siirtojen_maara % 2 == 0:
            paras_valinta = minimax(kopio_lauta, int(syvyys), -np.inf, np.inf, siirtojen_maara, False, 0, 0)[1]
            return paras_valinta
        paras_valinta = minimax(kopio_lauta, int(syvyys), -np.inf, np.inf, siirtojen_maara, True, 0, 0)[1]
        return paras_valinta

def main():
    """Käynnistää ai vs ai pelin.
    """
    peli = Tekoaly_Peli()
    peli.peli_silmukka()

if __name__=="__main__":
    try:
        main()
    except pygame.error:
        print("Suljit pelin!")

import pygame
from pelilauta import PeliLauta
from tekoaly.paras_siirto import paras_siirto
from toiminnot import tarkista_voitto, sallittu_siirto, vapaa_rivi
from config import RIVIT, SARAKKEET, NAYTON_KOKO, FONT, TEKSTI_1_PAIKKA, TEKSTI_2_PAIKKA, SININEN, TUMMAN_SININEN,KELTAINEN, PUNAINEN, MUSTA, HARMAA

class Kayttoliittyma:
    """Luokka vastaa pelin käyttöliittymästä.
    """
    def __init__(self):
        pygame.init()
        self.peli = PeliLauta()
        self.naytto = pygame.display.set_mode(NAYTON_KOKO)
        self.kello = pygame.time.Clock()
        self.kaynnissa = True
        self.tasapeli = False
        self.vuoro = 42
        self.numero = -1
        self.ohje_teksti = "Valitse sarake (1-7)."
        self.font = pygame.font.SysFont(FONT, 28)
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

    def peli_silmukka(self):
        """Pelin silmukka. Käy läpi tapahtumat, päivittää ja tulostaa näytön.
        """
        self.peli.uusi_peli()
        self.piirra_naytto()
        while self.kaynnissa:
            if self.vuoro % 2 == 0:
                self.numero = -1
                self.tapahtumat()
                if not self.siirto(self.numero, 1):
                    self.ohje_teksti = "Valinta ei ole mahdollinen. Valitse nmr 1-7."
                    continue
            else:
                self.tapahtumat()
                sarake = paras_siirto(self.peli.lauta, self.vuoro)
                if not self.siirto(sarake, 2):
                    self.ohje_teksti = "ei löydä saraketta"
                self.ohje_teksti = "Valitse sarake (1-7)!"
            self.paivita()
            self.piirra_naytto()
        while True:
            self.tapahtumat()
            if self.tasapeli:
                self.ohje_teksti = "Tasapeli!"
            else:
                if self.vuoro % 2 == 0:
                    self.ohje_teksti = "Hävisit!"
                else:
                    self.ohje_teksti = "Voitit Pelin! :D"
            self.piirra_naytto()

    def tapahtumat(self):
        """Käy läpi pelaajan syötteet.
        """
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                self.kaynnissa = False
                pygame.quit()
            if self.kaynnissa:
                if tapahtuma.type == pygame.KEYDOWN:
                    if self.vuoro % 2 == 0:
                        self.numero = (tapahtuma.key-49)

    def valikko(self):
        """Tämä tulee vastaamaan aloita alusta yms toiminnoista.
        """
        pass

    def piirra_naytto(self):
        """Piirtää laudan ja tekstit.
        """
        self.naytto.fill(HARMAA)
        pygame.draw.rect(self.naytto, SININEN, pygame.Rect(60, 60, 350, 300))
        for rivi in range(RIVIT):
            for sarake in range(SARAKKEET):
                if self.peli.lauta[rivi][sarake] == 1:
                    väri = KELTAINEN
                elif self.peli.lauta[rivi][sarake] == 2:
                    väri = PUNAINEN
                else:
                    väri = TUMMAN_SININEN
                pygame.draw.circle(self.naytto, väri, (30+51*(sarake+1), 30+51*(rivi+1)),23)
                teksti = self.font.render(str(sarake+1), True, MUSTA)
                self.naytto.blit(teksti, (25+51*(sarake+1), 360))
        teksti_1 = self.font.render("Tervetuloa!", True, MUSTA)
        self.naytto.blit(teksti_1, (TEKSTI_1_PAIKKA))
        teksti_2 = self.font.render(self.ohje_teksti, True, MUSTA)
        self.naytto.blit(teksti_2, (TEKSTI_2_PAIKKA))
        pygame.display.update()
        self.kello.tick(60)

    def paivita(self):
        """Tarkistaa voiton ja tasapelin. Päivittää vuoron.
        """
        if tarkista_voitto(self.peli.lauta, self.peli.viimeisin_siirto):
            self.kaynnissa = False
        if self.vuoro == 1:
            self.tasapeli = True
            self.kaynnissa = False
        self.vuoro -= 1
        if self.vuoro % 2 != 0:
            self.ohje_teksti = "Odota vuoroasi!"

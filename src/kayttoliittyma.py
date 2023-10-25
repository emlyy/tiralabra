import pygame
from pelilauta import PeliLauta
from tekoaly.minimax import paras_siirto
from toiminnot import tarkista_voitto, sallittu_siirto, vapaa_rivi
from config import (RIVIT, SARAKKEET, NAYTON_KOKO, FONT, TEKSTI_1_PAIKKA,
    TEKSTI_2_PAIKKA, SININEN, TUMMAN_SININEN, KELTAINEN,
    PUNAINEN, MUSTA, HARMAA, TEKSTI_3_PAIKKA, VALITSE, LAUTA_X, LAUTA_Y, LEVEYS, KORKEUS, REUNA, HALKASIJA, LISA_X)

class Kayttoliittyma:
    """Luokka vastaa pelin käyttöliittymästä.
    """
    def __init__(self):
        pygame.init()
        self.peli = PeliLauta()
        self.naytto = pygame.display.set_mode(NAYTON_KOKO)
        self.kello = pygame.time.Clock()
        self.kaynnissa = False
        self.aloitus = True
        self.tasapeli = False
        self.resetointi = False
        self.vuoro = 42
        self.numero = -1
        self.hiiri = (250,0)
        self.pelaaja_vari = KELTAINEN
        self.ai_vari = PUNAINEN
        self.vuoro_lisa = 0
        self.ohje_teksti = VALITSE
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

    def aloitus_naytto(self):
        """Silmukka, joka suorittaa aloitus näytön.
        """
        while self.aloitus:
            self.piirra_aloitus_naytto()
            self.tapahtumat()

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
                if (self.vuoro+self.vuoro_lisa) % 2 == 0:
                    self.ohje_teksti = "Hävisit!"
                    self.teksti_vari = PUNAINEN
                else:
                    self.ohje_teksti = "Voitit Pelin! :D"
                    self.teksti_vari = SININEN
            self.piirra_naytto()

    def peli_silmukka(self):
        """Pelin silmukka. Käy läpi tapahtumat, päivittää ja tulostaa näytön.
        """
        self.peli.uusi_peli()
        self.piirra_naytto()
        while self.kaynnissa:
            # Pelaajan vuoro; tarkistaa pelaajan syötteet
            if (self.vuoro+self.vuoro_lisa) % 2 == 0:
                self.numero = -1
                self.tapahtumat()
                if self.resetointi:
                    self.aloita_alusta()
                    self.peli_silmukka()
                    break
                if self.numero == -1:
                    self.piirra_naytto()
                    continue
                if not self.siirto(self.numero, 1):
                    continue
            # Tietokoneen vuoro; etsitään paras siirto minimaxilla
            else:
                self.tapahtumat()
                sarake = paras_siirto(self.peli.lauta, self.vuoro)
                if not self.siirto(sarake, 2):
                    self.ohje_teksti = "ongelma"
                    continue
                self.ohje_teksti = VALITSE
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
                # Pyydetään valitsemaan aloittaja
                if self.aloitus:
                    if tapahtuma.key == pygame.K_k:
                        self.valitse(1)
                    if tapahtuma.key == pygame.K_p:
                        self.valitse(2)
                # Tarkistetaan jos uudelleen aloitus
                elif tapahtuma.key == pygame.K_ESCAPE:
                    self.resetointi = True
            if self.kaynnissa:
                # Päivitetään pelaajan hiiren sijainti seuraavaa siirtoa varten
                if (self.vuoro+self.vuoro_lisa) % 2 == 0:
                    if tapahtuma.type == pygame.MOUSEMOTION:
                        hiiri = pygame.mouse.get_pos()
                        if REUNA <= hiiri[0] <= LAUTA_X+LEVEYS:
                            self.hiiri = hiiri
                    if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                        self.numero = (self.hiiri[0]-REUNA)//HALKASIJA

    def valitse(self, valinta):
        """Alustukset sen mukaan kumpi aloittaa.

        Args:
            valinta (int): 1: pelaaja aloittaa, 2: ai aloittaa.
        """
        if valinta == 1:
            self.pelaaja_vari = KELTAINEN
            self.ai_vari = PUNAINEN
            self.vuoro_lisa = 0
        else:
            self.pelaaja_vari = PUNAINEN
            self.ai_vari = KELTAINEN
            self.vuoro_lisa = 1
        self.aloitus = False
        self.kaynnissa = True

    def aloita_alusta(self):
        """Aloittaa pelin alusta.
        """
        self.resetointi = False
        self.kaynnissa = True
        self.tasapeli = False
        self.vuoro = 42
        self.numero = -1
        self.peli.uusi_peli()
        self.ohje_teksti = VALITSE

    def piirra_aloitus_naytto(self):
        """Piirtää aloitusnäytön.
        """
        self.naytto.fill(HARMAA)
        teksti_1 = self.font.render("Tervetuloa!", True, MUSTA)
        self.naytto.blit(teksti_1, (TEKSTI_1_PAIKKA))
        teksti_2 = self.font.render("paina k jos haluat aloittaa", True, MUSTA)
        self.naytto.blit(teksti_2, (10,100))
        teksti_3 = self.font.render("paina p jos haluat ai:n aloittavan", True, MUSTA)
        self.naytto.blit(teksti_3, (10,150))
        pygame.display.update()

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
        if (self.vuoro+self.vuoro_lisa) % 2 == 0:
            pygame.draw.circle(self.naytto, self.pelaaja_vari, (self.hiiri[0], 125),HALKASIJA/2)
        for rivi in range(RIVIT):
            for sarake in range(SARAKKEET):
                if self.peli.lauta[rivi][sarake] == 1:
                    väri = self.pelaaja_vari
                elif self.peli.lauta[rivi][sarake] == 2:
                    väri = self.ai_vari
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
        if (self.vuoro+self.vuoro_lisa) % 2 != 0:
            self.ohje_teksti = "Odota vuoroasi!"

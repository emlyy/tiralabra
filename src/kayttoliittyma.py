import pygame
from pelilauta import PeliLauta
from tekoaly.minimax import paras_siirto, paras_siirto_tekoaly_peli
from toiminnot import tarkista_voitto, sallittu_siirto, vapaa_rivi
from config import (RIVIT, SARAKKEET, NAYTON_KOKO, FONT, TEKSTI_1_PAIKKA,
    TEKSTI_2_PAIKKA, SININEN, TUMMAN_SININEN, KELTAINEN, PUNAINEN, MUSTA,
    HARMAA, TEKSTI_3_PAIKKA, VALITSE, LAUTA_X, LAUTA_Y, LEVEYS, KORKEUS,
    REUNA, HALKASIJA, LISA_X, SYVYYS_KELT, SYVYYS_PUN)

class Kayttoliittyma:
    """Luokka vastaa pelin käyttöliittymästä.
    """
    def __init__(self):
        pygame.init()
        self.peli = PeliLauta()
        self.naytto = pygame.display.set_mode(NAYTON_KOKO)
        self.kello = pygame.time.Clock()
        self.ai_peli = False
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
            self.tapahtumat_aloitus()

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

    def tapahtumat_aloitus(self):
        """Käy läpi käyttäjän syötteet aloitusnäytön aikana.
        """
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_k:
                    self.valitse_aloittaja(1)
                if tapahtuma.key == pygame.K_p:
                    self.valitse_aloittaja(2)
                if tapahtuma.key == pygame.K_a:
                    self.valitse_aloittaja(3)

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
            if self.kaynnissa:
                if not self.ai_peli and (self.vuoro+self.vuoro_lisa) % 2 == 0:
                    if tapahtuma.type == pygame.MOUSEMOTION:
                        hiiri = pygame.mouse.get_pos()
                        if REUNA <= hiiri[0] <= LAUTA_X+LEVEYS:
                            self.hiiri = hiiri
                    if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                        self.numero = (self.hiiri[0]-REUNA)//HALKASIJA

    def valitse_aloittaja(self, valinta: int):
        """Alustukset sen mukaan kumpi aloittaa tai jos valitaan tekoäly peli.

        Args:
            valinta (int): 1: pelaaja aloittaa, 2: ai aloittaa,
            3: ai vs ai peli.
        """
        self.pelaaja_vari = KELTAINEN
        self.ai_vari = PUNAINEN
        self.vuoro_lisa = 0
        if valinta == 2:
            self.pelaaja_vari = PUNAINEN
            self.ai_vari = KELTAINEN
            self.vuoro_lisa = 1
        elif valinta == 3:
            self.ai_peli = True
            self.ohje_teksti = "Keltainen aloittaa"
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
        self.ohje_teksti = "uusi peli"
        self.teksti_vari = MUSTA

    def piirra_aloitus_naytto(self):
        """Piirtää aloitusnäytön.
        """
        self.naytto.fill(HARMAA)
        self.teksti("Tervetuloa", TEKSTI_1_PAIKKA, MUSTA)
        self.teksti("paina k jos haluat aloittaa", (10,100), MUSTA)
        self.teksti("paina p jos haluat ai:n aloittavan", (10,150), MUSTA)
        self.teksti("paina a jos katso ai vs ai pelin", (10,200), MUSTA)
        pygame.display.update()

    def teksti(self, sanat, koordinaatit, vari):
        teksti = self.font.render(sanat, True, vari)
        self.naytto.blit(teksti, (koordinaatit))

    def piirra_naytto(self):
        """Piirtää laudan ja tekstit.
        """
        self.naytto.fill(HARMAA)
        self.piirra_pelilauta()
        self.teksti("Tervetuloa", TEKSTI_1_PAIKKA, MUSTA)
        self.teksti(self.ohje_teksti, TEKSTI_2_PAIKKA, self.teksti_vari)
        self.teksti("Aloita peli alusta painamalla ESC.", TEKSTI_3_PAIKKA, MUSTA)
        pygame.display.update()
        self.kello.tick(30)

    def piirra_pelilauta(self):
        """Vastaa pelilaudan piirtämisestä.
        """
        pygame.draw.rect(self.naytto, SININEN, pygame.Rect(LAUTA_X, LAUTA_Y, LEVEYS, KORKEUS))
        if not self.ai_peli:
            self.piirra_hiiri()
        for rivi in range(RIVIT):
            for sarake in range(SARAKKEET):
                if self.peli.lauta[rivi][sarake] == 1:
                    väri = self.pelaaja_vari
                elif self.peli.lauta[rivi][sarake] == 2:
                    väri = self.ai_vari
                else:
                    väri = TUMMAN_SININEN
                pygame.draw.circle(self.naytto, väri,
                    (LISA_X+(HALKASIJA+2)*(sarake+1), REUNA+(HALKASIJA+2)*(rivi+1)),
                    HALKASIJA/2)

    def piirra_hiiri(self):
        """Piirtää ylhäällä liikutettavan seuraavan palan.
        """
        if (self.vuoro+self.vuoro_lisa) % 2 == 0:
            pygame.draw.circle(self.naytto, self.pelaaja_vari, (self.hiiri[0], 125),HALKASIJA/2)

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
            if self.ai_peli:
                self.ohje_teksti = "Punaisen vuoro"

    def lopetus_naytto_tekoaly_peli(self):
        """Silmukka, joka suorittaa lopetus näytön tekoäly pelille.

        Piirtää näytön ja tarkistaa pelaajan syötteitä uudelleen aloittamisen varalta.
        """
        while True:
            self.tapahtumat()
            if self.resetointi:
                self.aloita_alusta()
                self.peli_silmukka_tekoaly_peli()
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

    def peli_silmukka_tekoaly_peli(self):
        """Pelin silmukka kun ai vs ai peli. Käy läpi tapahtumat, päivittää ja tulostaa näytön.
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
            if self.resetointi:
                self.aloita_alusta()
                self.peli_silmukka_tekoaly_peli()
                break
            if syvyys <= 9:
                pygame.time.wait(2000)
            sarake = paras_siirto_tekoaly_peli(self.peli.lauta, self.vuoro, syvyys)
            if not self.siirto(sarake, pelaaja):
                self.ohje_teksti = "ongelma"
                continue
            self.ohje_teksti = "Keltaisen vuoro"
            self.paivita()
            self.piirra_naytto()
        self.lopetus_naytto_tekoaly_peli()

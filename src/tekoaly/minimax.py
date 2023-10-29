from copy import deepcopy
import numpy as np
from toiminnot import tarkista_voitto, siirra, vapaa_rivi
from tekoaly.pisteytys import pisteyta
from config import SYVYYS, JARJESTYS

def paras_siirto(lauta: list, siirtojen_maara: int):
    """Kokeilee siirtovaihtoehdot keskeltä ulospäin käyttäen minimax algoritmia ja
       valitsee parhaan siirron.

    Args:
        lauta (list): Pelilaudan tämänhetkinen tilanne.
        siirtojen_maara (int): Kertoo kuinka monta siirtoa on jäljellä tasapeliin.

    Returns:
        int: Palauttaa valitun sarakkeen.
    """
    kopio_lauta = deepcopy(lauta)
    paras_valinta = (
        minimax(kopio_lauta, int(SYVYYS), -np.inf, np.inf, siirtojen_maara, True, 0, 0)[1])
    return paras_valinta

def paras_siirto_tekoaly_peli(lauta: list, siirtojen_maara: int, syvyys: int):
    """Valitsee parhaan siirron minimax algoritmin avulla vuorotellen tekoäly pelaajille.
    Käytetään ai vs ai pelissä.

    Args:
        lauta (list): Pelilaudan tämänhetkistä tilannetta kuvaava matriisi.
        siirtojen_maara (int): Kertoo kuinka monta siirtoa on jäljellä tasapeliin.
        syvyys (int): syvyys mikä halutaan käydä läpi minimaxilla.

    Returns:
        int: Palauttaa valitun sarakkeen.
    """
    kopio_lauta = deepcopy(lauta)
    if siirtojen_maara % 2 == 0:
        paras_valinta = (
            minimax(kopio_lauta, int(syvyys), -np.inf, np.inf, siirtojen_maara, False, 0, 0)[1])
        return paras_valinta
    paras_valinta = (
        minimax(kopio_lauta, int(syvyys), -np.inf, np.inf, siirtojen_maara, True, 0, 0)[1])
    return paras_valinta

def minimax(pelilauta: list, syvyys: int, alfa: float|int, beta: float|int,
            siirtojen_maara: int, ai_vuoro: bool, edellinen_rivi: int, edellinen_sarake: int):
    """Minimax algoritmi alfa-beta karsinnalla.

    Args:
        pelilauta (list): Matriisi pelilaudan tilanteesta.
        syvyys (int): Puun syvyys.
        alfa (float or int): Minimiarvo, jonka max varmasti saa. Alkuun -inf.
        beta (float or int): Enimmäisarvo, jonka min varmasti saa. Alkuun inf.
        siirtojen_maara (int): Siirtojen määrä tasapeliin.
        ai_vuoro (boolean): Kertoo onki max/ai vuoro.
        edellinen_rivi (int): Edellisen siirron rivi.
        edellinen_sarake (int): Edellisen siirron sarake.

    Returns:
        Palauttaa heuristisen arvon ja siirron.
    """
    pelaaja = 1
    if ai_vuoro:
        pelaaja = 2
    if tarkista_voitto(pelilauta, (edellinen_rivi, edellinen_sarake)):
        if ai_vuoro:
            return -500000*(syvyys+1), None
        return 500000*(syvyys+1), None
    if syvyys == 0 or siirtojen_maara == 0:
        arvo = pisteyta(pelilauta, pelaaja, syvyys)
        if not ai_vuoro:
            arvo = -arvo
        return arvo, None
    if ai_vuoro:
        paras_arvo = -np.inf
        for siirto in JARJESTYS:
            kopio_pelilauta = deepcopy(pelilauta)
            rivi = vapaa_rivi(kopio_pelilauta, siirto)
            if rivi is None:
                continue
            siirra(kopio_pelilauta, rivi, siirto, 2)
            uusi_arvo = (minimax(
                kopio_pelilauta, syvyys-1, alfa, beta, siirtojen_maara-1, False, rivi, siirto)[0])
            if uusi_arvo > paras_arvo:
                paras_valinta = siirto
                paras_arvo = uusi_arvo
            alfa = max(alfa, paras_arvo)
            if beta <= alfa:
                break
        return paras_arvo, paras_valinta
    paras_arvo = np.inf
    for siirto in JARJESTYS:
        kopio_pelilauta = deepcopy(pelilauta)
        rivi = vapaa_rivi(kopio_pelilauta, siirto)
        if rivi is None:
            continue
        siirra(kopio_pelilauta, rivi, siirto, 1)
        uusi_arvo = (minimax(
            kopio_pelilauta, syvyys-1, alfa, beta, siirtojen_maara-1, True, rivi, siirto)[0])
        if uusi_arvo < paras_arvo:
            paras_valinta = siirto
            paras_arvo = uusi_arvo
        beta = min(beta, uusi_arvo)
        if beta <= alfa:
            break
    return paras_arvo, paras_valinta

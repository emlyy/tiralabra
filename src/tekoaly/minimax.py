import numpy as np
from toiminnot import tarkista_voitto, siirra, vapaa_rivi
from tekoaly.pisteytys import pisteyta
from config import JARJESTYS

def minimax(pelilauta, syvyys: int, alfa: float|int, beta: float|int,
            siirtojen_maara: int, ai_vuoro: bool, edellinen_rivi: int, edellinen_sarake: int):
    """Minimax algoritmi alfa-beta karsinnalla.

    Args:
        pelilauta (_type_): Matriisi pelilaudan tilanteesta.
        syvyys (int): Puun syvyys.
        alfa (float or int): Minimiarvo, jonka max varmasti saa. Alkuun -inf.
        beta (float or int): Enimmäisarvo, jonka min varmasti saa. Alkuun inf.
        siirtojen_maara (int): Siirtojen määrä tasapeliin.
        ai_vuoro (boolean): Kertoo onki max/ai vuoro.
        edellinen_rivi (int): Edellisen siirron rivi.
        edellinen_sarake (int): Edellisen siirron sarake.

    Returns:
        int or float: Palauttaa heuristisen arvon.
    """
    pelaaja = 1
    if ai_vuoro:
        pelaaja = 2
    if tarkista_voitto(pelilauta, (edellinen_rivi, edellinen_sarake)):
        if ai_vuoro:
            return -500000, None
        return 500000, None
    if syvyys == 0 or siirtojen_maara == 0:
        arvo = pisteyta(pelilauta, pelaaja)
        if not ai_vuoro:
            arvo = -arvo
        return arvo, None
    if ai_vuoro:
        paras_arvo = -np.inf
        for siirto in JARJESTYS:
            kopio_pelilauta = np.copy(pelilauta)
            rivi = vapaa_rivi(kopio_pelilauta, siirto)
            if rivi is None:
                continue
            siirra(kopio_pelilauta, rivi, siirto, 2)
            uusi_arvo = minimax(kopio_pelilauta, syvyys-1, alfa, beta, siirtojen_maara-1, False,
                                rivi, siirto)[0]
            if uusi_arvo > paras_arvo:
                paras_valinta = siirto
                paras_arvo = uusi_arvo
            alfa = max(alfa, paras_arvo)
            if beta <= alfa:
                break
        return paras_arvo, paras_valinta
    paras_arvo = np.inf
    for siirto in JARJESTYS:
        kopio_pelilauta = np.copy(pelilauta)
        rivi = vapaa_rivi(kopio_pelilauta, siirto)
        if rivi is None:
                continue
        siirra(kopio_pelilauta, rivi, siirto, 1)
        uusi_arvo = minimax(kopio_pelilauta, syvyys-1, alfa, beta, siirtojen_maara-1, True, rivi,
                            siirto)[0]
        if uusi_arvo < paras_arvo:
            paras_valinta = siirto
            paras_arvo = uusi_arvo
        beta = min(beta, uusi_arvo)
        if beta <= alfa:
            break
    return paras_arvo, paras_valinta

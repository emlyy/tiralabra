import numpy as np
from config import SARAKKEET
from toiminnot import vapaa_rivi, siirra
from minimax import minimax

def paras_siirto(lauta):
    paras_arvo = -np.inf
    paras_valinta = 3
    for siirto in range(SARAKKEET):
        rivi = vapaa_rivi(lauta, siirto)
        #kopio pelilauta, break jos sarake täynnä
        siirra(kopio_lauta,rivi,siirto, 2)
        arvo = minimax(lauta, 5, True)
        if arvo > paras_arvo:
            paras_valinta = siirto
            paras_arvo = arvo
    return paras_valinta

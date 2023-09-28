import numpy as np
from config import SARAKKEET
from toiminnot import vapaa_rivi, siirra, sallittu_siirto
from tekoaly.minimax import minimax

def paras_siirto(lauta, siirtojen_maara: int):
    """Kokeilee siirtovaihtoehdot keskeltä ulospäin käyttäen minimax algoritmia ja valitsee parhaan siirron. 

    Args:
        lauta (_type_): Pelilaudan tämänhetkinen tilanne.
        siirtojen_maara (int): Kertoo kuinka monta siirtoa on jäljellä tasapeliin.

    Returns:
        int: Palauttaa valitun sarakkeen.
    """
    paras_arvo = -np.inf
    paras_valinta = 3
    for siirto in [3,4,2,5,1,6,0]:
        if not sallittu_siirto(lauta, siirto):
            continue
        kopio_lauta = np.copy(lauta)
        rivi = vapaa_rivi(lauta, siirto)
        siirra(kopio_lauta, rivi, siirto, 2)
        arvo = minimax(kopio_lauta, 5, -np.inf, np.inf, siirtojen_maara, False, rivi, siirto)
        if arvo > paras_arvo:
            paras_valinta = siirto
            paras_arvo = arvo
    return paras_valinta

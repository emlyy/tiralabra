import numpy as np
from config import JARJESTYS, SYVYYS
from toiminnot import vapaa_rivi, siirra, sallittu_siirto
from tekoaly.minimax import minimax

def paras_siirto(lauta, siirtojen_maara: int):
    """Kokeilee siirtovaihtoehdot keskeltä ulospäin käyttäen minimax algoritmia ja
       valitsee parhaan siirron.

    Args:
        lauta (_type_): Pelilaudan tämänhetkinen tilanne.
        siirtojen_maara (int): Kertoo kuinka monta siirtoa on jäljellä tasapeliin.

    Returns:
        int: Palauttaa valitun sarakkeen.
    """
    kopio_lauta = np.copy(lauta)
    paras_valinta = minimax(kopio_lauta, SYVYYS, -np.inf, np.inf, siirtojen_maara, True, 0, 0)[1]
    return paras_valinta

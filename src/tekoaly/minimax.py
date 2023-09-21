import numpy as np
from pelilauta import PeliLauta, Toiminnot

def minimax(pelilauta, syvyys, ai_vuoro):
    """Minimax algoritmi. Käy siirrot läpi ja valitsee parhaan vaihtoehdon.

    Args:
        pelilauta (_type_): Matriisi pelilaudan tilanteesta.
        syvyys (int): Puun syvyys.
        ai_vuoro (boolean): Kertoo onko max/ai vuoro.

    Returns:
        _type_: Palauttaa heuristisen arvon tai valitun siirron.
    """
    if syvyys == 0 or Toiminnot.taynna() or Toiminnot.tarkista_voitto():
        # laske arvo
        return arvo
    if ai_vuoro:
        arvo = -np.inf
        for siirto in range(7):
            # lisää siirto pelilaudalle
            arvo = max(arvo, minimax(pelilauta, syvyys-1, False))
        return arvo
    arvo = np.inf
    for siirto in range(7):
        # lisää siirto pelilaudalle
        arvo = min(arvo, minimax(pelilauta, syvyys-1, True))
    return arvo

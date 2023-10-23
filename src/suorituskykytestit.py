import time
import numpy as np
from tekoaly.minimax import minimax

def minimax_suoritus_aika(pelilauta, syvyys, siirtojen_maara, rivi, sarake):
    """Mittaa sekunneissa, kuinka kauan minimaxilla kestää käydä siirrot läpi annetulla syvyydellä.

    Args:
        pelilauta: Matriisi pelilaudan tilanteesta.
        syvyys (int): Syvyys, joka halutaan käydä läpi.
        siirtojen_maara (int): Siirtojen määrä tasapeliin.
        rivi (_type_): Edellisen siirron rivi.
        sarake (_type_): Edellisen siirron sarake.

    Returns:
        str: Palauttaa syvyyden ja keston sekunneissa.
    """
    aloitus_aika = time.perf_counter()
    minimax(pelilauta, syvyys, -np.inf, np.inf, siirtojen_maara, True, rivi, sarake)
    lopetus_aika = time.perf_counter()
    kesto = lopetus_aika - aloitus_aika
    return f"Syvyys {syvyys} kesto: {kesto:.3}s"

if __name__=="__main__":
    lauta = np.array([
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [2, 2, 2, 1, 2, 1, 0]])
    print(minimax_suoritus_aika(lauta, 5, 33, 4, 2))
    print(minimax_suoritus_aika(lauta, 6, 33, 4, 2))
    print(minimax_suoritus_aika(lauta, 7, 33, 4, 2))
    print(minimax_suoritus_aika(lauta, 8, 33, 4, 2))
    print(minimax_suoritus_aika(lauta, 9, 33, 4, 2))
    print(minimax_suoritus_aika(lauta, 10, 33, 4, 2))

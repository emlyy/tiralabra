from config import RIVIT, SARAKKEET

"""Pelilaudan päivittämiseen liittyviä toimintoja.
"""
def siirra(lauta, rivi: int, sarake: int, vuoro: int):
    """Päivittää siirron annettuun matriisiin.

    Args:
        lauta (_type_): Pelilaudan tilannetta kuvaava matriisi.
        rivi (int): Rivi johon pala tippuu.
        sarake (int): Valittu sarake.
        vuoro (int): Pelaajan vuoro: 1. Tietokoneen vuoro: 2.
    """
    lauta[rivi][sarake] = vuoro

def sallittu_siirto(lauta, sarake: int):
    """Tarkistaa, onko pelilaudalla valitussa sarakkeessa tilaa.

    Args:
        lauta: Pelilaudan tilannetta kuvaava matriisi.
        sarake (int): Valittu sarake.

    Returns:
        boolean: Palauttaa True, jos sarakkeessa on vielä tilaa. False jos
        sarake täynnä tai ei kuulu laudalle.
    """
    if sarake in range(SARAKKEET):
        return lauta[0][sarake] == 0
    return False

def vapaa_rivi(lauta, sarake: int):
    """Tarkistaa mihin seuraava pala tiputetaan.

    Args:
        lauta: Pelilaudan tilannetta kuvaava matriisi.
        sarake (int): Valittu sarake.

    Returns:
        int: Palauttaa sarakkeessa alimman vapaana olevan rivin, mihin pala tippuu.
    """
    for rivi in range(RIVIT-1,-1,-1):
        if lauta[rivi][sarake] == 0:
            return rivi
    return None

def tarkista_voitto(lauta, viimeisin_siirto: tuple):
    """Tarkistaa onko toinen pelaajista saanut neljän suoran.

    Args:
        lauta: Pelilaudan tilannetta kuvaava matriisi.
        viimeisin_siirto (tuple): (x,y) missä x rivi ja y sarake.

    Returns:
        boolean: Palauttaa True, jos löytyy neljän suora, muuten palauttaa False.
    """
    for sarake in range(SARAKKEET-3):
        if (lauta[viimeisin_siirto[0]][sarake] ==
            lauta[viimeisin_siirto[0]][sarake+1] ==
            lauta[viimeisin_siirto[0]][sarake+2] ==
            lauta[viimeisin_siirto[0]][sarake+3] != 0):
            return True
    for rivi in range(RIVIT-3):
        if (lauta[rivi][viimeisin_siirto[1]] ==
            lauta[rivi+1][viimeisin_siirto[1]] ==
            lauta[rivi+2][viimeisin_siirto[1]] ==
            lauta[rivi+3][viimeisin_siirto[1]] != 0):
            return True
    for rivi in range (RIVIT-3):
        for sarake in range(SARAKKEET-3):
            if (lauta[rivi][sarake] == lauta[rivi+1][sarake+1] ==
                lauta[rivi+2][sarake+2] == lauta[rivi+3][sarake+3] != 0):
                return True
    for rivi in range (3,RIVIT):
        for sarake in range(SARAKKEET-3):
            if (lauta[rivi][sarake] == lauta[rivi-1][sarake+1] ==
            lauta[rivi-2][sarake+2] == lauta[rivi-3][sarake+3] != 0):
                return True
    return False

from config import RIVIT, SARAKKEET

def pisteyta(lauta, pelaaja: int):
    """Arvioi pelaajan aseman pelissä.

    Args:
        lauta (_type_): Pelilaudan tilannetta kuvaava matriisi.
        pelaaja (int): Kumman näkökulmasta peliä arvioidaan. 1: pelaaja, 2: tekoäly.

    Returns:
        int: Palauttaa lasketun arvon. Mitä suurempi arvo sitä paremmassa asemassa
        arvioitava pelaaja on.
    """
    arvo = (tarkista_varma_kolme(lauta, pelaaja) + pisteytys_vaaka(lauta, pelaaja) +
            pisteytys_pysty(lauta, pelaaja) + pisteytys_laskeva_viisto(lauta, pelaaja) +
            pisteytys_nouseva_viisto(lauta, pelaaja))
    return arvo

def tarkista_varma_kolme(lauta, pelaaja: int):
    """Tarkistaa onko kolmen suoraa, jonka molemmilla puolilla vapaa pelattava tila.
    """
    arvo = 0
    for sarake in range(SARAKKEET-4):
        for rivi in range(RIVIT):
            if lauta[rivi][sarake] == lauta[rivi][sarake+4] == 0 and (
            lauta[rivi][sarake+1] == lauta[rivi][sarake+2] ==
            lauta[rivi][sarake+3] != 0):
                if rivi == 5 or (lauta[rivi+1][sarake] != 0 and lauta[rivi+1][sarake+4] != 0):
                    if lauta[rivi][sarake+1] == pelaaja:
                        arvo = 500000
                    else:
                        arvo = -500000
                    return arvo
    return arvo

def pisteytys_vaaka(lauta, pelaaja):
    """Tarkistaa onko kolmen vaakasuora, missä toisella puolella vapaa pelattava tila.
    """
    arvo = 0
    for sarake in range(SARAKKEET-2):
        for rivi in range(RIVIT):
            if (lauta[rivi][sarake] ==
                lauta[rivi][sarake+1] ==
                lauta[rivi][sarake+2] != 0):
                if (sarake-1 in range(SARAKKEET) and lauta[rivi][sarake-1] == 0) or (
                    sarake+3 in range(SARAKKEET) and lauta[rivi][sarake+3] == 0):
                    if lauta[rivi][sarake+1] == pelaaja:
                        arvo += 10000
                    else:
                        arvo -= 9000
    return arvo

def pisteytys_pysty(lauta, pelaaja):
    """Tarkistaa onko kolmen pystysuora, missä pelattava tila yläpuolella.
    """
    arvo = 0
    for rivi in range(RIVIT-2):
        for sarake in range(SARAKKEET):
            if (lauta[rivi][sarake] ==
                lauta[rivi+1][sarake] ==
                lauta[rivi+2][sarake] != 0):
                if rivi-1 in range(RIVIT) and lauta[rivi-1][sarake] == 0:
                    if lauta[rivi][sarake] == pelaaja:
                        arvo += 10000
                    else:
                        arvo -= 9000
    return arvo

def pisteytys_laskeva_viisto(lauta, pelaaja):
    """Tarkistaa onko kolmen suora viistosti, missä toisella puolella vapaa tila.
    """
    arvo = 0
    for rivi in range (RIVIT-2):
        for sarake in range(SARAKKEET-2):
            if (lauta[rivi][sarake] == lauta[rivi+1][sarake+1] ==
                lauta[rivi+2][sarake+2] != 0):
                if ((rivi-1 in range(RIVIT) and sarake-1 in range(SARAKKEET)) and
                    lauta[rivi-1][sarake-1] == 0) or (
                    (rivi+3 in range(RIVIT) and sarake+3 in range(SARAKKEET)) and
                    lauta[rivi+3][sarake+3] == 0):
                    if lauta[rivi][sarake] == pelaaja:
                        arvo += 10000
                    else:
                        arvo -= 9000
    return arvo

def pisteytys_nouseva_viisto(lauta, pelaaja):
    """Tarkistaa onko kolmen suora viistosti, missä toisella puolella vapaa tila.
    """
    arvo = 0
    for rivi in range (2,RIVIT):
        for sarake in range(SARAKKEET-2):
            if (lauta[rivi][sarake] == lauta[rivi-1][sarake+1] ==
            lauta[rivi-2][sarake+2] != 0):
                if ((rivi+1 in range(RIVIT) and sarake-1 in range(SARAKKEET)) and
                    lauta[rivi+1][sarake-1] == 0) or (
                    (rivi-3 in range(RIVIT) and sarake+3 in range(SARAKKEET)) and
                    lauta[rivi-3][sarake+3] == 0):
                    if lauta[rivi][sarake] == pelaaja:
                        arvo += 10000
                    else:
                        arvo -= 9000
    return arvo

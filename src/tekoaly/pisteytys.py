import numpy as np
from config import RIVIT, SARAKKEET

def tarkista_varma_kolme(lauta):
    """Tarkistaa onko kolmen suoraa, jonka molemmilla puolilla vapaa tila.
    """
    arvo = 0
    for sarake in range(SARAKKEET-4):
        for rivi in range(RIVIT):
            if lauta[rivi][sarake] == lauta[rivi][sarake+4] == 0 and (
            lauta[rivi][sarake+1] == lauta[rivi][sarake+2] ==
            lauta[rivi][sarake+3] != 0):
                if rivi == 5 or (lauta[rivi+1][sarake] != 0 and lauta[rivi+1][sarake+4] != 0):
                    if lauta[rivi][sarake+1] == 1:
                        arvo = -np.inf
                    else:
                        arvo = np.inf
                    return arvo
    return arvo

def pisteytys(lauta):
    """Tarkistaa onko kolmen suoraa.
    """
    arvo = 0
    for sarake in range(SARAKKEET-2):
        for rivi in range(RIVIT):
            if (lauta[rivi][sarake] ==
                lauta[rivi][sarake+1] ==
                lauta[rivi][sarake+2] != 0):
                if (sarake-1 in range(SARAKKEET) and lauta[rivi][sarake-1] == 0) or (
                    sarake+3 in range(SARAKKEET) and lauta[rivi][sarake+3] == 0):
                    if lauta[rivi][sarake+1] == 1:
                        arvo -= 9000
                    else:
                        arvo += 9000
    for rivi in range(RIVIT-2):
        for sarake in range(SARAKKEET):
            if (lauta[rivi][sarake] ==
                lauta[rivi+1][sarake] ==
                lauta[rivi+2][sarake] != 0):
                if rivi-1 in range(RIVIT) and lauta[rivi-1][sarake] == 0:
                    if lauta[rivi][sarake] == 1:
                        arvo -= 9000
                    else:
                        arvo += 9000
    for rivi in range (RIVIT-2):
        for sarake in range(SARAKKEET-2):
            if (lauta[rivi][sarake] == lauta[rivi+1][sarake+1] ==
                lauta[rivi+2][sarake+2] != 0):
                if (rivi-1 in range(RIVIT) and lauta[rivi-1][sarake-1] == 0) or (
                    rivi+3 in range(RIVIT) and lauta[rivi+3][sarake+3] == 0):
                    if lauta[rivi][sarake] == 1:
                        arvo -= 9000
                    else:
                        arvo += 9000
    for rivi in range (2,RIVIT):
        for sarake in range(SARAKKEET-2):
            if (lauta[rivi][sarake] == lauta[rivi-1][sarake+1] ==
            lauta[rivi-2][sarake+2] != 0):
                if (rivi+1 in range(RIVIT) and lauta[rivi+1][sarake-1] == 0) or (
                    rivi-3 in range(RIVIT) and lauta[rivi-3][sarake+3] == 0):
                    if lauta[rivi][sarake] == 1:
                        arvo -= 9000
                    else:
                        arvo += 9000
    return arvo

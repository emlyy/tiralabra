import pygame
from kayttoliittyma import Kayttoliittyma
def tekoaly_peli():
    """Käynnistää ai vs ai pelin.
    """
    peli = Kayttoliittyma()
    peli.valitse_aloittaja(3)
    peli.peli_silmukka_tekoaly_peli()

if __name__=="__main__":
    try:
        tekoaly_peli()
    except pygame.error:
        print("Suljit pelin!")

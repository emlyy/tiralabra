import pygame
from kayttoliittyma import Kayttoliittyma

def main():
    """Käynnistää pelin.
    """
    peli = Kayttoliittyma()
    peli.aloitus_naytto()
    peli.peli_silmukka()

if __name__=="__main__":
    try:
        main()
    except pygame.error:
        print("Suljit pelin!")

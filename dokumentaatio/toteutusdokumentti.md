# Toteutusdokumentti

## Yleisrakenne
Ohjelman rakennetta kuvaava luokkakaavio:

```mermaid
classDiagram
    Kayttoliittyma "1" -- "1" PeliLauta
    Kayttoliittyma "1" -- Toiminot
    PeliLauta "1" -- Toiminnot
    Kayttoliittyma "1" -- paras_siirto
    Kayttoliittyma <|-- paras_siirto
    paras_siirto -- minimax
    minimax <|-- paras_siirto
    minimax "1" -- "1" PeliLauta
    minimax <|-- pisteytys
    minimax "1" -- pisteytys
    minimax -- Toiminnot

    class Kayttoliittyma {
        -peli_silmukka()
        -siirto()
    }

    class PeliLauta {
        -uusi_peli()
        -paivita_lauta()
    }

    class Toiminnot {
        -siirra()
        -taynna()
        -sallittu_siirto()
        -vapaa_rivi()
        -tarkista_voitto()
    }
```

## Aika- ja tilavaativuudet

## Työn mahdolliset puutteet ja parannusehdotukset
- Minimax käy vaihtoehdot aina keskeltä ulospäin, jotta voidaan käydä isompi syvyys.
- Pelivalikko, mahdollisuus aloitta alusta/uudelleen

## Lähteet

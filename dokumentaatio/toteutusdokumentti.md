# Toteutusdokumentti

## Yleisrakenne
Ohjelman rakennetta kuvaava luokkakaavio:

```mermaid
classDiagram
    Kayttoliittyma "1" -- "1" PeliLauta
    Kayttoliittyma "1" -- Toiminnot
    PeliLauta "1" -- Toiminnot
    Kayttoliittyma "1" -- paras_siirto
    Kayttoliittyma <|-- paras_siirto
    paras_siirto <|-- minimax
    minimax "7" -- "1" paras_siirto
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
- Mahdollisuus palata takaisin aloitusnäytölle.
- Seuraavaksi tiputettava pala liikkuu pelilaudan ulkopuollelle.
- Minimax valitsee varman myöhemmän voiton heti pelattavan voiton sijaan joskus.

## Lähteet

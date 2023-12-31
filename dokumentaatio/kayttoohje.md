# Käyttöohje

## Asennus ja käynnistys Poetryn avulla
1. Kloonaa repositorio tai lataa viimeisimmän [releasen](https://github.com/emlyy/tiralabra/releases/tag/loppupalautus) lähdekoodi.
2. (Asenna [Poetry](https://python-poetry.org/docs/)). Asenna riippuvuudet komennolla:
```
poetry install
```
3. Käynnistä ohjelma komennolla:
```
poetry run invoke start
```
4. Jos haluat käynnistää pelkän tekoäly vs tekoäly pelin käytä komentoa:
```
poetry run invoke tekoaly
```

## Peli
- Valitse ensin haluatko aloittaa pelin. (Painamalla k aloittaa, p tietokone aloittaa pelin. Painamalla a voit käynnistää tekoäly vastaan tekoäly pelin)
- Voit valita seuraavan siirtosi liikuttamalla ja painamalla hiirtä.
- Voit aloitta pelin uudelleen painamalla esc-näppäintä.

## Konfiguraatio
Jos haluat vaihtaa puun läpikäytävää syvyyttä:
```
config.py rivit 14-16
SYVYYS = os.getenv("SYVYYS") or 8   # normaalin pelin syvyys
SYVYYS_KELT = 4    # tekoäly vs tekoäly pelin keltainen pelaaja
SYVYYS_PUN = 7     # tekoäly vs tekoäly pelin punainen pelaaja
```

Testeissä käytetty syvyys on konfiguroitu .env.test -tiedostossa:
```
.env.test rivi 3
SYVYYS = 5
```

## Muita komentoja
Testit voi ajaa komennolla:
```
poetry run invoke test
```
Lisätietoa testeistä [testausdokumentissa](./testausdokumentti.md).

Pylint komennolla:
```
poetry run invoke lint
```
Kaikki komennot löytyvät [tasks.py](/tasks.py)-tiedostosta.

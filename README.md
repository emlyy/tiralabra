# Connect Four

Helsingin yliopiston aineopintojen harjoitustyö: Algoritmit ja tekoäly

## Dokumentaatio
- [käyttöohje](dokumentaatio/kayttoohje.md)
- [määrittelydokumentti](dokumentaatio/maarittelydokumentti.md)
- [testausdokumentti](dokumentaatio/testausdokumentti.md)
- [toteutusdokumentti](dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit
- [viikko 1](dokumentaatio/viikkoraportti-1.md)
- [viikko 2](dokumentaatio/viikkoraportti-2.md)
- [viikko 3](dokumentaatio/viikkoraportti-3.md)

## Hyödyllisiä komentoja
Peli käynnistyy komennolla:
```
poetry run invoke start
```
Testikattavuus raportti generoituu htmlcov-hakemistoon komennolla:
```
poetry run invoke coverage-report
```
Testit komennolla:
```
poetry run invoke test
```
Pylint:
```
poetry run invoke lint
```
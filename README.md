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
- [viikko 4](dokumentaatio/viikkoraportti-4.md)
- [viikko 5](dokumentaatio/viikkoraportti-5.md)
- [viikko 6](dokumentaatio/viikkoraportti-6.md)
- [viikkot 7 ja 8](dokumentaatio/viikkoraportti-7-8.md)

## Hyödyllisiä komentoja
Peli käynnistyy komennolla:
```
poetry run invoke start
```
Voit käynnistää tekoäly vastaan tekoäly pelin komennolla:
```
poetry run invoke tekoaly
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

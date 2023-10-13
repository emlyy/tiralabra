# Viikkoraportti 6

## Mitä olen tehnyt?/Miten ohjelma on edistynyt?
Tällä viikolla olen työstänyt käyttöliittymää ja parannellut minimaxia. Pelin alussa on nyt aloitusnäyttö, jossa voi valita kumpi pelaaja aloittaa pelin. Myös sarakkeen valinta on muutettu näppäimistöllä tehdystä valinnasta, hiirellä toimivaan valintaan. Muokkaisin paras_siirto ja minimaxia siten, että minimax palauttaa arvon ja parhaan siirron. Paras_siirto ei enään arvioi kaikkia seitsemää siirtoa erikseen, vaan kutsuu suoraan minimaxia kerran.

## Mitä opin tällä viikolla?
Opin, että välillä kun pelaa tekoälyä vastaan, se ei valitse voittoa, koska sillä on välittömän voiton lisäksi toinen varma voitto parin siirron päästä. 
Ehkä voisin erikseen käydä 1 syvyydellä kaikki 7 siirtoa ja jos jokin niistä palauttaa min tai maks niin ei tarvitse käydä valitulla syvyydellä minimaxia, vaan tehdään seuraava siirto voitoksi tai blokkausta varten.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Jos valitsen syvyydeksi 8-10, parhaan siirron valitseminen kestää kauan, kun pelaan peliä pygamella. Kuitenkin jos suoritan pelkälle minimaxille syvyydellä 10 suorituskykytestin kesto on alle 4 sekuntia. Pygame:n pelisilmukalla on varmaan jotain vaikutusta tälle.

## Mitä teen seuraavaksi?
Yritän selvittää yllä mainittuja asioita ja jatkan dokumentaation kirjoittamista.

## Työhön käytetty aika
| pvm | h | mitä tein |
| :--- | ---: | :--- |
| 9.10 | 1 | suunnittelu, turhien funktioiden poisto |
| 11.10 | 1 | käyttöliittymä |
| 12.10 | 3 | vertaisarvionti |
| 13.10 | 6 | dokumentaatio, käyttöliittymä, minimax parantelua |
| yht | 11 tuntia |

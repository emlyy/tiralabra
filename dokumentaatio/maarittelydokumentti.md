# Määrittelydokumentti

### Kieli
Käytän ohjelmointikielenä Pythonia. En hallitse muita ohjelmointikieliä vertaisarviontia varten. Projektin dokumentaatio, koodi ja kommentit ovat suomeksi. Vertaisarvionti onnistuu myös englanniksi.

### Aihe
Toteutan Connect Four pelille tekoälyn, jota vastaan voi pelata. Valitsin Connect Four:n projektin aiheeksi, koska halusin valita pelin, joka on minulle ennestään tuttu.

## Projektissa käytettävät algoritmit ja tietorakenteet

### Algoritmit
- minimax
  - saadaan valittua tekoälyn seuraava siirto

- alpha-beta-karsinta
  - karsitaan tutkittavia siirtoja

### Tietorakenteet
Pelilaudan tilanteen seuraamiseksi tulen käyttämään matriisia.

### Aika ja tila vaativuudet
Minimax-algoritmin aikavaativuus on O(b^m), missä b on vaihtoehtoisten siirtojen määrä, ja m on puun suurin syvyys [1]. Tila vaativuus O(bm). Alpha beta karsinnan kanssa pahin mahdollinen aikavaativuus on sama kuin minimax, eli puu joudutaan käymään kokonaan läpi. Paras aikavaativuus on O(b^(d/2)), missä d on syvyys.

### Opinto-ohjelma
Opiskelen tietojenkäsittelytieteen kandidaatin tutkintoa (TKT).

### Lähteet
[1] Vasileios Megalooikonomou, [CIS603-Artificial Intelligence](https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html)

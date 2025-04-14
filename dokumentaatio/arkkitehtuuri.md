# Arkkitehtuurikuvaus

## Luokkakaavio

```mermaid
classDiagram

    class Laatta {
        -arvo: int 2^x
    }

    class Pelilauta {
        -4x4 ruudukko
        -pisteitä: int
    }

    class Siirto {
        - Vasemmalle
        - Oikealle
        - Ylös
        - Alas
    }

    Pelilauta --> AlustaPeli
    Pisteitä"Pisteita: 0" -- AlustaPeli
    AlustaPeli -- UusiLaatta
    UusiLaatta "2" -- Laatta
    UusiLaatta "90%" -- Laatta2
    UusiLaatta "10%" -- Laatta4
    Pelilauta -- Siirto
    Siirto "2 samaa" --> Yhdistys
    Laatta -- Siirto
    Yhdistys "Laattojen summa" -- Pistelaskuri
    Pistelaskuri -- Pisteitä
    Siirto --> UusiLaatta

```


## Pakkauskaavio


```mermaid
graph TD
    ui --> services
    services --> enteties 
```
Pakkaus *ui* käytää *services* pakkauksessa olevaa pelilogiikkaa. *services* käyttää *entities* pakkausta sillä siellä ovat *Board* ja *Tile*.


## Käyttöliittymä
Käyttäjällä on kolme mahdollista näkymää
1. Alkunäyttö
   - Tulee esille vain avatessa pelin
   - Pelaaja voi aloittaa pelin tai poistua
2. Pelinäkymä
   - Missä itse peli sijaisee
   - Pelaaja myös näkee tämänhetkiset pisteet
3. Häviö näkymä
   - Tulee häviämisen jälkeen automaattisesti
   - Pelaaja näkee että peli loppui ja saamansa pisteet
   - Pelaaja voi aloittaa uudelleen tai poistua
   

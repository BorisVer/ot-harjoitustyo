# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/BorisVer/ot-harjoitustyo/releases/tag/viikko6) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

Asenna riippuvuudet komennolla
```
poetry install
```
Käynnistä peli komennolla
```
poetry run invoke start
```

## Pelin pelaaminen
Peli avautuu alkunäyttöön, josta "Start Game" nappia painamalla peli käynnistyy. Peliä pelataan nuolinäppäimmillä. Nuolinäppäintä painaessa kaikki pelikentän laatat liukuvat kyseiseen suuntaan kunnes osuvat reunaan tai toiseen laattaa. Jos kaksi saman arvoista laattaa yhdistyy niistä syntyy yksi tuplasti arvokkaampi laatta. Tästä saa laattojen summan verran lisää pisteitä. Pelin tavoite on saada mahdollisimman paljon pisteitä. Peli loppuu kun koko ruutu on tukossa eikä ole yhtäkään mahdollista siirtoa enään. 


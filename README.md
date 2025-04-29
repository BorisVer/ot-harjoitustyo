 # 2048 Peli

Pelin idea on saman arvoisten laattojen yhdistäminen suurempi arvoisiin laattoihin. Yhdistäminen tapahtuu siirroilla (vasemmalle, oikeall, ylös, alas) ja lopullisena tavoitteena on saavuttaa 2048 arvoinen ruutu. 

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Change Log](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Relese](https://github.com/BorisVer/ot-harjoitustyo/releases/tag/viikko5)
- [Käyttöohje](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
 
## Asennus
1. Asenna riippuvuudet

   ```bash
   poetry install
   ```
   
2. Avaa peli

   ```bash
   poetry run invoke start
   ```

## Ohjelman suoritukset

### Pelin voi käynnistää
   ```bash
   poetry run invoke start
   ```

### Testit voi suorittaa
   ```bash
   poetry run invoke test
   ```

### Pylint testin voi suorittaa
   ```bash
   poetry run invoke lint
   ```


### Coverage raportin voi saada
   ```bash
   poetry run invoke coverage-report
   ```
Raportti ilmestyy *htmlcov* hakemustoon

 # 2048

2048 Peli

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Change Log](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/BorisVer/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
 
## Asennus
1. Asenna riippuvuudet

   ```bash
   poetry install
   ```
   
2. Avaa peli

   ```bash
   poetry run invoke start
   ```

### Ohjelman suoritukset

Pelin voi käynnistää
   ```bash
   poetry run invoke start
   ```

Testit voi suorittaa
   ```bash
   poetry run invoke test
   ```

Coverage raportin voi saada
   ```bash
   poetry run invoke coverage-report
   ```

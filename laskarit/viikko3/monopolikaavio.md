
```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Monopolipeli "1" -- Aloitusruutu
    Monopolipeli "1" -- Vankila

    Ruutu -- Aloitusruutu
    Ruutu -- Vankila
    Ruutu -- Sattuma
    Ruutu -- Yhteismaa
    Ruutu -- Asema
    Ruutu -- Laitos
    Ruutu -- Katu

    Kortit -- Sattuma
    Kortit -- Yhteismaa
    Toiminto -- Kortit
    Toiminto -- Aloitusruutu
    Toiminto -- Vankila
    Toiminto -- Asema
    Toiminto -- Laitos
    Toiminto -- Katu


    Talo "0..4" -- Katu
    Hotelli "0..1" -- Katu

    Katu -- Pelaaja
    Pelaaja -- Rahaa



```

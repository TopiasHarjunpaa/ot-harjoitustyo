# Ohjelmistotekniikka, kevät 2021
### The Possible Game | harjoitustyö

The Possible Game on ohjelmistotekniikan kurssin harjoitustyö. Sovellus on yksinkertainen tasohyppelypeli, jonka esikuvana toimii [The Impossible Game](https://impossible.game/). Pelissä pelaajan tulee väistellä vastaan tulevia esteitä ja edetä mahdollisimman pitkälle. Tarkemmat tiedot löytyvät dokumentaatiosta.

## Releaset

- [Viikko 5 -release](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko 6 -release](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus -release](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/releases/tag/v1.0)

## Dokumentaatio

- [Käyttöohje](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

## Asennus

Aloita kloonaamalla repositorio:

```
$ git clone git@github.com:TopiasHarjunpaa/ot-harjoitustyo.git
$ cd ot-harjoitustyo
```

Asenna seuraavaksi tarvittavat riippuvuudet ja alusta tietokanta komennoilla:

```
$ poetry install
$ poetry run invoke build
```

Ohjelma käynnistetään komennolla:

```
$ poetry run invoke start
```

## Muut komentorivitoiminnot


#### Testaus:

Testit voidaan suorittaa komennolla:

```
poetry run invoke test
```

Testikattavuusraportin saa generoitua komennolla:

```
poetry run invoke coverage-report
```

Raportti generoidaan kansioon nimeltä `htmlcov`. Käyttöliittymään ja testeihin liittyvä koodi on jätetty raportista pois.

#### Pylint:

Laatutarkastukset voidaan suorittaa komennolla:

```
poetry run invoke lint
```

Käyttöliittymään ja testeihin liittyvä koodi on jätetty pois laatutarkastuksista.

## Credits

Fontti:
* Ladattu osoitteesta [dafont](https://www.dafont.com/no-virus.font)
* Tekijä **Khurasan**

Musiikki:
* Ladattu osoitteesta [OpenGameArt](https://opengameart.org/content/5-chiptunes-action)
* Tekijä **Juhani Junkala**

Ääniefektit:
* Luotu työkalulla [Bfxr](https://www.bfxr.net/)

Taustakuvat:
* Luotu [Enscape](https://enscape3d.com/)



# Ohjelmistotekniikka, kevät 2021
### The Possible Game | harjoitustyö

The Possible Game on ohjelmistotekniikan kurssin harjoitustyö. Tarkemmat tiedot löytyvät dokumentaatiosta.

## Release

Projektista on tehty GitHub release (0.25p)
Release sisältää ohjelman uusimman version lähdekoodin (GitHub-lisää tämän automaattisesti releasin tehdessä)
Ohje releasen tekemiseen
Releaseen on linkki projektin README:stä

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

Placeholder...
Lisää fontit, musiikki yms...

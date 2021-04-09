# Ohjelmistotekniikka, kevät 2021
### The Possible Game | harjoitustyö

The Possible Game on ohjelmistotekniikan kurssin harjoitustyö. Tarkemmat tiedot löytyvät dokumentaatiosta.

## Dokumentaatio

- [Käyttöohje (placeholder)]()
- [Vaatimusmäärittely](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus (placeholder)]()
- [Testausdokumentti (placeholder)]()
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

## Komentorivitoiminnot

#### Ohjelman suorittaminen:

```
poetry run invoke start
```

#### Testaus:

```
poetry run invoke test
```

#### Testikattavuus:

```
poetry run invoke coverage-report
```

#### Pylint:

```
poetry run invoke lint
```
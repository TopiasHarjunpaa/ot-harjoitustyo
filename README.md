# Ohjelmistotekniikka, kevät 2021
### The Possible Game | harjoitustyö

## Dokumentaatio

- [Käyttöohje (placeholder)]()
- [Vaatimusmäärittely](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus (placeholder)]()
- [Testausdokumentti (placeholder)]()
- [Työaikakirjanpito](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

## Asennus

Asenna komennolla:

```
poetry install
```

Suorita komennolla:

```
poetry run invoke build
```

Käynnistä komennolla:

```
poetry run invoke start
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
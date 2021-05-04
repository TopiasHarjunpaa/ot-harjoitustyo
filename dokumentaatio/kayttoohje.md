# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/releases/tag/viikko5)

## Konfigurointi

Tietokannan nimeä voi muuttaa *.env-tiedostossa*. Testitietokannan nimeä voi muuttaa *.env.test-tiedostossa*. Molemmat tietokannat luodaan automaattisesti *data-kansioon* niiden puuttuessa.

## Asennus ja käynnistäminen

Asenna aluksi tarvittavat riippuvuudet ja alusta tietokanta komennoilla:

```
$ poetry install
$ poetry run invoke build
```

Ohjelma käynnistetään komennolla:

```
$ poetry run invoke start
```

## Pelaaminen

### Ohjelman käynnistäminen avaa aloitusvalikon:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-menu.png" width="700">

Aloitusvalikossa näytetään TOP3 -tulokset. Pelaaja voi:
1. Aloittaa uuden pelin painamalla näppäimistöllä kirjainta `N`
2. Ladata aiemman pelin painamalla näppäimistöllä kirjainta `L`
3. Poistua pelistä painamalla `ESC` tai sivun ylälaidassa olevaa raksia.

### Pelaajan siirtyessä uuden pelin aloittamisnäkymään:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-new.png" width="700">

Uuden pelin aloittamisnäkymässä pelaaja pyydetään syöttämään neljä kirjaiminen nimimerkki (numeroja sekä erikoismerkkejä ei hyväksytä). Nimimerkki toimii myös tunnisteena, jonka avulla pelaaja voi myöhemmin jatkaa samaa tallennusta.

Nimimerkin syöttämisen jälkeen pelaajalla avautuu mahdollisuus jatkaa eteenpäin pelin käynnistysnäkymään painamalla `ENTER`. Paluu takaisin aloitusvalikkoon tapahtuu painamalla `ESC`.

### Pelaajan siirtyessä lataamaan aiempaa peliä:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-load.png" width="700">

Aiemman pelin lataamisnäkymässä näytetään korkeintaan 8 tallennettua peliä. Tallennetut pelit ovat järjestettynä edistymistilanteen mukaan, joten valittavista vaihtoehdoista katoavat pienimmän edistyksen omaavat pelit tilanteissa, joissa luotuja peleja on enemmän kuin 8 kappaletta.

Tallennetun pelin voi valita painamalla näppäintä `1 - 8` riippuen siitä, millä rivillä valittu peli sijaitsee listalla. Paluu takaisin aloitusvalikkoon tapahtuu painamalla `ESC`.

### Pelin valitsemisen jälkeen siirrytään pelin käynnistysnäkymään:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-start.png" width="700">

Käynnistysnäkymässä näytetään pelin tunnisteena käytetty nimimerkki sekä kokonaisedistyminen prosenteissa. Kunkin uuden tason läpäiseminen kasvattaa kokonaisedistymistä yhteensä 100 prosenttiyksiköllä. Vastaavasti uudessa tasossa puoleen väliin pääseminen kasvattaa kokonaisedistymistä 50 prosenttiyksiköllä. Maksimiedistyminen on siis `tasojen lkm * 100%` eli tässä tapauksessa 400%.

Aluksi pelaaja voi valita vain ensimmäisen tason muiden tasojen ollessa lukittuna. Kunkin tason läpäiseminen avaa oikeuden pelata seuraavaa tasoa. Tason käynnistäminen tapahtuu painamalla näppäintä `1 - tasojen lukumäärä`. Paluu takaisin aloitusvalikkoon tapahtuu painamalla `ESC`.

### Tason käynnistäminen avaa pelinäkymän:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-game.png" width="700">

Pelissä ruudun keskellä on purppuran värinen neliö, joka kuvaa pelaajan hahmoa. Pelaajan hahmo liikkuu automaattisesti kohti maalia ja pelaajan tehtävänä on hyppiä näppäimellä `SPACE` kohti maalia väistellen sinisiä hahmoja sekä välttäen koskemasta *laavaan*. Peli päättyy mikäli pelaaja koskettaa sinisiä hahmoja tai laavaa.

Näytön yläreunassa kerrotaan tason numero sekä pelin edetessä kasvavat prosentit, jotka kuvaavat kyseisen tason edistymistä.

Pelin voi keskeyttää painamalla `ESC` joka palauttaa pelaajan takaisin pelin käynnistysnäkymään.

### Pelaajan kuolema avaa Game Over näkymän:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-game-over.png" width="700">

Game Over näkymässä pelaajalle kerrotaan kyseisen tason edistyminen prosentteina sekä aiempi ennätys. Mikäli äskeinen tulos on parempi kuin aiempi ennätys, niin siitä muodostuu uusi ennätys ja myös pelaajan kokonaisedistyminen päivitetään vastaamaan uutta tulosta.

Pelaaja voi jatkaa pelaamista painamalla `ENTER`, jolloin näytetään pelin käynnistysnäkymä. Paluu takaisin aloitusvalikkoon tapahtuu painamalla `ESC`.

### Tason läpäiseminen avaa Level Completed näkymän:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-level-finish.png" width="700">

Level Completed näkymässä pelaajalle näytetään tason aiempi ennätys. Mikäli tasoa ei ollut aiemmin läpäisty, niin päivitetään pelaajan kokonaisedistyminen ja avataan mahdollisuus yrittää seuraavaa tasoa.

Pelaaja voi jatkaa pelaamista painamalla `ENTER`, jolloin näytetään pelin käynnistysnäkymä. Nyt käynnistysnäkymässä on avoinna uusi tasoja, jota pääsee yrittämään. Paluu takaisin aloitusvalikkoon tapahtuu painamalla `ESC`.
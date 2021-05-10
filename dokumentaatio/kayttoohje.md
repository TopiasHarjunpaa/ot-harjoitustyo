# Käyttöohje

Lataa projektin viimeisin [release (viikko 6)](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/releases/tag/viikko6)

## Konfigurointi

Tietokannan sekä testitietokannan nimiä voi muuttaa kansioissa `-env` sekä `.env.test`. Molemmat tietokannat luodaan automaattisesti `data` -kansioon niiden puuttuessa.

Myös tiedostojen nimiä voidaan muuttaa `.env` -kansiossa. Huomaa, että tiedostonimien tulee vastata [assets](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/tree/main/src/assets) -kansioon luotujen tiedostojen nimiä. Muussa tapauksessa ohjelman suoritus päättyy `FileNotFoundError` -virheeseen.

```
DATABASE_FILENAME=TPG_database.sqlite
LEVEL0_FILENAME=level_0.csv
LEVEL1_FILENAME=level_1.csv
LEVEL2_FILENAME=level_2.csv
LEVEL3_FILENAME=level_3.csv
LEVEL4_FILENAME=level_4.csv
FONT_FILENAME=fontstyle.ttf
MENU_BG_FILENAME=menu_background.png
LEVEL1_BG_FILENAME=level1_background.jpg
LEVEL2_BG_FILENAME=level2_background.jpg
LEVEL3_BG_FILENAME=level3_background.jpg
LEVEL4_BG_FILENAME=level4_background.jpg
MENU_MUSIC_FILENAME=menu.ogg
LEVEL1_MUSIC_FILENAME=level1.ogg
LEVEL2_MUSIC_FILENAME=level2.ogg
LEVEL3_MUSIC_FILENAME=level3.ogg
LEVEL4_MUSIC_FILENAME=level4.ogg
BACK_SOUND_FILENAME=back.wav
DIE_SOUND_FILENAME=die.wav
JUMP_SOUND_FILENAME=jump.wav
FORWARD_SOUND_FILENAME=forward.wav
KEY_SOUND_FILENAME=key.wav
```

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
3. Avata asetusvalikon painamalla näppäimistöllä kirjainta `S`
4. Poistua pelistä painamalla `ESC` tai sivun ylälaidassa olevaa raksia.

### Pelaajan siirtyessä asetusvalikkoon:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjekuva-settings.png" width="700">

Asetusvalikossa pelaaja voi säätää ääniasetuksia. Musiikki ja ääniefektit ovat oletusarvoisestä päällä pelin käynnistyessä. Pelaaja voi:
1. Poistaa musiikin päältä painamalla näppäimistöllä numeroa `1`
2. Poistaa ääniefektit päältä painamalla näppäimistöllä numeroa `2`
3. Musiikin ja ääniefektin saa takaisin päälle painamalla samaa numeroa `1 tai 2`uudelleen
4. Palata takaisin aloitusvalikkoon painamalla `ESC`

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
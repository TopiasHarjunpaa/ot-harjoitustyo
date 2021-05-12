# Testausdokumentti

Ohjelmaa on testattu yksikkö- ja integraatiotestien avulla.

## Yksikkö- ja integraatiotestaus

#### Entities-luokat

Useimmat `Entities` -luokkien toiminnallisuudet ovat testattu integraatiotasolla sovelluslogiikan yhteydessä. Yksikkötestejä on kuitenkin suoritettu seuraaville luokille:

[TestObstacle](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/entities/obstacle_test.py) -luokalla testataan, että luotu olio poistetaan omasta ryhmästä sen poistuessa näytön ulkopuolelle.

[TestPlayer](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/entities/player_test.py) -luokalla testataan `jump()` -metodin toimintaa olion ollessa lattialla sekä ilmassa.

[TestSave](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/entities/save_test.py) -luokalla testataan `get_information()` -metodin toimintaa erilaisilla `progress` -attribuutin arvoilla.

[TestSprites](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/entities/sprites_test.py) -luokalla testataan, että `Sprite` -ryhmien alustaminen luo kaikki oikeat ryhmät.

#### Repositorio-luokka

Ohjelmassa on vain yksi Repositorio-luokka `SaveRepository`, jota testaan [TestSaveRepository](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/repositories/save_repository_test.py) -luokan avulla. Testauksessa käytetään testitietokantaa, jonka nimi on konfiguroitu `.env.test` -tiedostoon.

#### Sovelluslogiikka

Sovelluslogiikka testataan seuraavien testiluokkien avulla:

[TestAudioService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/services/audio_service_test.py) -luokalla testataan äänien toistamisesta vastaavan luokan metodeita. Testeissä tarkastetaan, että kaikki sovellukseen kuuluvat äänitiedostot toimivat toivotunlaisesti myös silloin, kun äänet ovat asetettu päälle tai pois päältä.

[TestGameService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/services/game_service_test.py) -luokalla testataan peliloopin toimivuutta. Tähän lukeutuvat testit testaavat pelin läpäisemistä, kuolemaa sekä painikkeiden toimivuutta. Testejä varten käytetään seuraavia valeluokkia:

* `StubClock`
* `StubEventQueue`
* `StubRenderer`
* `StubAudio`
* `StubUI`

Kuhunkin valeluokkaan on luotu testien kannalta tarpeettomat funktiot, joita kuitenkin kutsutaan alkuperäisen `GameService` -luokan metodikutsuissa.

[TestInformationService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/services/information_service_test.py) -luokalla testataan tiedon välityksen toiminnallisuutta `SaveRepository` -luokan tietokantakyselyiden sekä käyttöliittymän `UI` -luokan välillä. Testit ovat hyvin pitkälle samankaltaisia `TestSave` sekä `TestSaveRepository` -luokkien kanssa.

[TestLevelService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/tests/services/level_service_test.py) -luokalla testataan pelitason toiminnallisuuksia, kuten pelaajan hyppäämistä, kuolemista tai tason läpäisemistä.

## Testikattavuus

Testikattavuusraportin saa generoitua komennolla:

```
poetry run invoke coverage-report
```

Raportti generoidaan kansioon nimeltä `htmlcov`. Käyttöliittymään ja testeihin liittyvä koodi on jätetty raportista pois. Testauksen haarautumakattavuus

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/testikattavuus.png" width="1000">

Testaamatta jäivät: 
* `build.py` sekä `initialize_database.py` suorittaminen komentoriviltä
* `config.py` FileNotFoundError -virheen toimivuus tilanteissa, joissa tiedostoa ei löydy
* `player.py` ääniefektin toimivuus hyppytilanteessa. Tämä on kuitenkin testattu yksikkötasoilla testiluokissa `TestPlayer`, `TestLevelService` sekä `TestAudioService`.
* `game_service.py` pelin sulkemista varten toteutetun `quit()` -metodin kutsuminen käyttöliittymäolion avulla.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

#### Asennus ja konfigurointi

Sovellus on haettu ja testattu [käyttöohjeessa](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md) kuvatulla tavalla Linux-ympäristössä sekä etätyöpöytää käyttämällä.

Sovellusta on testattu tilanteissa, joissa tietokannat ovat olleet olemassa sekä tilanteissa, joissa niitä ei ole vielä luotu. Lisäksi tiedostonimien muuttamista on testattu muuttamalla `.env` sekä [assets](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/tree/main/src/assets) -kansiossa olevia tiedostonimiä toisenlaisiksi.

#### Toiminnallisuudet

Kaikki tasot ovat testattu ja pelattu läpi 1920 x 1080 resoluution näyttöasetuksilla (osa tasoista myös 1600 x 900). Objektien koot sekä tapahtumien nopeus ovat pyritty pitämään lähes tulkoon saman kokoisena huolimatta käytetystä resoluutiosta. Sen sijaan hyppäämiseen liittyvät parametrit noudattavat vakioitua pikselikokoa. Tästä syystä pelin läpäiseminen muuttuu hyvin hankalaksi pienillä resoluutiolla.

Käyttöliittymän siirtymissä sekä syötteiden antamisessa ei ole havaittu virheitä manuaalisen testauksen avulla.


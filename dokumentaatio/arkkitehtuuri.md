# Arkkitehtuurikuvaus

## Rakenne

Pakkaus ja luokkakaavio tarvitsee päivitystä...

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus-luokat.png" width="1000">

## UI

Placeholder...

## Sovelluslogiikka

Placeholder...

## Tallennus

Placeholder...

## Päätoiminnallisuudet

Ohjelman päätoiminnallisuudet kuvattuna sekvenssikaavioiden avulla:

### Ohjelman alustaminen

Ohjelman alustaminen tapahtuu tiedostossa [index.py](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/index.py). Aluksi alustetaan pygame, tarkastetaan näytön koko sekä asetetaan pelille otsikko. Sitten alustetaan seuraavat luokat sekvenssikaavion mukaisesti:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-ohjelman-alustaminen.png" width="1000">

Luokkien alustaminen tapahtuu melko suoraviivaisesti.`InformationService` -luokan yhteydessä luodaan samalla tietokantayhteys sekä alustetaan `SaveRepository`, joka huolehtii tietokantakyselyistä pelin ainoaan tietokantatauluun liittyen. Peli käynnistyy kutsumalla `UI` -luokan metodia `start_menu()`.

### Peliluokkien alustaminen

Aiemmassa sekvenssikaaviossa kuvattiin ohjelman alustaminen sekä käynnistäminen. Tarkemmin ottaen `UI` -luokan alustamisen yhteydessä luodaan myös peliluokat `LevelService` ja `GameService` seuraavan sekvenssikaavion mukaisesti:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-peliluokkien-alustaminen.png" width="1000">

`LevelService` -luokan alustamiseen tarvitaan näytön mitat sekä tasonumero. Vapaaehtoisena parametrina voidaan antaa myös audioluokka.`LevelService` -luokka alustaa peliin liittyvät objektit luokan `Sprites` avulla. `Sprites` luo tasonumeron perusteella kyseiseen tasoon liittyvät objektit kuten lattian, esteet sekä pelihahmon. `GameService` -luokan alustamista varten `UI` välittää saamansa parametrit `InformationService`:ä lukuunottamatta.

### Menunäkymä

Ensimmäiseksi pelin käynnistämisen jälkeen näytetään menunäkymä. Tämä aloitetaan kutsumalla `UI` -luokan metodia `show_menu_view()`. Seuraava sekvenssikaavio esittää menunäkymäkutsun etenemisen:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-menu.png" width="1000">

Aluksi pyydetään `AudioService` -luokkaa käynnistämään menunäkymän kappale (audioluokka on saanut audiotiedostojen polut alustamisen yhteydessä). Seuraavaksi haetaan TOP3 parhaat tulokset tietokannasta. `InformationService` kutsuu metodilla `find_all_saves()` tietokantakyselyjä tekevää `save_repository` -oliota hakemaan tulokset tietokannasta. Kolmesta parhaasta tuloksesta luodaan `Save` oliot ja palautetaan muuttujaan `records`. Seuraavaksi kutsutaan `MenuView` -luokan metodia `show()`, jolle annetaan parametrina aiemmin haetut tulokset. Tämän jälkeen `MenuView` -luokka erittelee tulokset ja kutsuu `Renderer` -luokan metodia `render_menu()`, joka lopulta renderöi menunäkymän ruudulle.

Kun menunäkymä on ruudulla, niin jäädään odottamaan käyttäjän syötettä. Mikäli käyttäjä painaa näppäintä `n`, niin siirrytään näyttämään uusipeli -näkymä. Mikäli käyttäjä painaa näppäintä `l`, niin siirrytään näyttämään lataapeli -näkymä.

### Uusipeli -näkymä

lisää tähän tekstiä...

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-new.png" width="1000">

lisää tähän tekstiä...

### Lataapeli -näkymä

lisää tähän tekstiä...

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-load.png" width="1000">

lisää tähän tekstiä...

### Käynnistäpeli -näkymä

lisää tähän tekstiä...

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-start.png" width="1000">

lisää tähän tekstiä...

### Pelin eteneminen

lisää puuttuva sekvenssikaavio ja tekstiä...

## Puutteet

Placeholder...
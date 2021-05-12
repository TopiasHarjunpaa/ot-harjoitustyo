# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne koostuu seuraavista pakkauksista:

1. Käyttöliittymä `ui`
2. Sovelluslogiikka `services`
3. Tietojen tallennus `repositories`
4. Tietokohteet ja objektit `entities`

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus-luokat.png" width="1000">

## UI

Käyttöliittymästä vastaa paketti `ui`, joka pitää sisällään seuraavat näkymät:

1. Aloitusvalikko `MenuView`
2. Asetukset `SetupView`
3. Uuden pelin aloittamisnäkymä `NewGameView`
4. Aiemman pelin latausnäkymä `LoadGameView`
5. Pelin käynnistysnäkymä `StartView`
6. Game Over -näkymä `GameOverView`
7. Level Completed -näkymä `FinishView`

Jokainen näistä on toteutettu omana luokkana. Näkymien näyttämisestä vastaa [UI](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/ui/ui.py) -luokka, joka käyttää apunaan näkymien piirtämisestä vastaavaa luokkaa [Renderer](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/ui/renderer.py).


## Sovelluslogiikka

Sovelluslogiista vastaa paketti `services`, joka pitää sisällään kolme päätehtävää:

1. Pelin ja tason toiminnallisuudet
2. Tiedon välittämisen
3. Äänen ja musiikin toistamisen.

Pelin ja tason toiminnallisuuksista vastaavat luokat [GameService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/services/game_service.py) sekä [LevelService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/services/level_service.py). Nämä huolehtivat pelitilanteen päivittämisestä sekä mahdollisesta pelin loppumisesta kuoleman tai maalin pääsemisen seurauksena. Näiden keskeisiä toiminnallisuuksia ovat mm:

* GameService luokan `start_gameloop(level)`, joka käynnistää peliloopin, alustaa uuden taso-olion tasonumeron perusteella, seuraa pelaajan komentoja sekä taso-olion tilaa.
* LevelService luokan `update()`, joka päivittää pelissä näytettävät objektit, ylläpitää pelitilannetta, laskee tasopisteitä sekä välittää tiedon pelin jatkumisesta `GameService` -luokalle.
* LevelService luokan metodit `player_is_alive()`, `handle_jump()` sekä `handle_goal()`, jotka tarkastavat törmäyksiä eri objektien välillä sekä mahdollistavat oikeat toimenpiteet näiden perusteella.

Tiedon välittämisestä vastaa [InformationService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/services/information_service.py) -luokka, joka pääsee tietoihin käsiksi tallennuksesta vastaavan `SaveRepository` -luokan kautta. `InformationService` tarjoaa käyttöliittymän `ui` -luokalle palvelut tiedon hakemista ja tallentamista varten. Keskeisiä toiminnallisuuksia ovat mm:

* `create_new_save(nickname)`
* `open_save(save_id)`
* `update_save(progress, save_id)`
* `get_progress_information()`
* `list_saves(number_of_saves)`

Äänen ja musiikin toistamisesta vastaa [AudioService](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/services/information_service.py) -luokka, joka huolehtii oikean ääniefektin tai musiikin toistamisesta tilanteeseen sopivalla tavalla. Keskeisiä toiminnallisuuksia ovat mm:

* `play_music(index)`
* `set_music_on()` sekä `set_music_off()`
* `set_sound_effects_on()` sekä `set_sound_effects_off()`
* `get_audio_information()`

## Tallennus

Tiedon tallentamisesta ja hakemisesta SQLite-tietokannasta huolehtii [SaveRepository](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/repositories/save_repository.py) -luokka. Sovellus hyödyntää yhtä tietokohdetta `Save`, joka pitää sisällään sovelluksen kannalta tarvittavan informaation, kuten pelitallenteen nimimerkin, edistymisen sekä luomispäivämäärän. 

SQLite tietokannassa vastaava tietokohde tallennetaan tauluun nimeltä `saves`. Taulun luomisesta vastaa [initialize_database.py](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/initialize_database.py). `SaveRepository` -luokka huolehtii tietokantakyselyistä tähän tauluun sekä välittää tietoa eteenpäin `Save` -olioiden avulla sovelluslogiikan `InformationService`:lle.

## Sovelluksen päätoiminnallisuudet

Ohjelman päätoiminnallisuudet kuvattuna sekvenssikaavioiden avulla:

### Ohjelman alustaminen

Ohjelman alustaminen tapahtuu tiedostossa [index.py](https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/src/index.py). Aluksi alustetaan pygame, tarkastetaan näytön koko sekä asetetaan pelille otsikko. Sitten alustetaan seuraavat luokat sekvenssikaavion mukaisesti:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-ohjelman-alustaminen.png" width="1000">

Luokkien alustaminen tapahtuu melko suoraviivaisesti. `InformationService` -luokan yhteydessä luodaan samalla tietokantayhteys sekä alustetaan `SaveRepository`, joka huolehtii tietokantakyselyistä pelin ainoaan tietokantatauluun liittyen. Peli käynnistyy kutsumalla `UI` -luokan metodia `start_menu()`.

### Peliluokkien alustaminen

Aiemmassa sekvenssikaaviossa kuvattiin ohjelman alustaminen sekä käynnistäminen. Tarkemmin ottaen `UI` -luokan alustamisen yhteydessä luodaan myös peliluokat `LevelService` ja `GameService` seuraavan sekvenssikaavion mukaisesti:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-peliluokkien-alustaminen.png" width="1000">

`LevelService` -luokan alustamiseen tarvitaan näytön mitat sekä tasonumero. Vapaaehtoisena parametrina voidaan antaa myös audioluokka. `LevelService` -luokka alustaa peliin liittyvät objektit luokan `Sprites` avulla. `Sprites` luo tasonumeron perusteella kyseiseen tasoon liittyvät objektit kuten lattian, esteet sekä pelihahmon. `GameService` -luokan alustamista varten `UI` välittää saamansa parametrit `InformationService`:ä lukuunottamatta.

### Menunäkymä

Ensimmäiseksi pelin käynnistämisen jälkeen näytetään menunäkymä. Tämä aloitetaan kutsumalla `UI` -luokan metodia `show_menu_view()`. Seuraava sekvenssikaavio esittää menunäkymäkutsun etenemisen:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-menu.png" width="1000">

Aluksi pyydetään `AudioService` -luokkaa käynnistämään menunäkymän kappale (audioluokka on saanut audiotiedostojen polut alustamisen yhteydessä). Seuraavaksi haetaan TOP3 parhaat tulokset tietokannasta. `InformationService` kutsuu metodilla `get_top_records(3)` tietokantakyselyjä tekevää `save_repository` -oliota hakemaan tulokset tietokannasta. Kolmesta parhaasta tuloksesta luodaan `Save` oliot ja palautetaan muuttujaan `records`. Seuraavaksi kutsutaan `MenuView` -luokan metodia `show()`, jolle annetaan parametrina aiemmin haetut tulokset. Tämän jälkeen `MenuView` -luokka erittelee tulokset ja kutsuu `Renderer` -luokan metodia `render_menu()`, joka lopulta renderöi menunäkymän ruudulle.

Kun menunäkymä on ruudulla, niin jäädään odottamaan käyttäjän syötettä: 
* Mikäli käyttäjä painaa näppäintä `n`, niin siirrytään näyttämään uusipeli -näkymä.
* Mikäli käyttäjä painaa näppäintä `l`, niin siirrytään näyttämään lataapeli -näkymä.
* Mikäli käyttäjä painaa näppäintä `s`, niin siirrytään näyttämään asetusnäkymä.

### Uusipeli -näkymä

Uusipeli -näkymä aloitetaan kutsumulla `UI` -luokan metodia `show_new_game_view()`. Seuraava sekvenssikaavio esittää uusipeli -näkymän etenemisen:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-new.png" width="1000">

Aluksi kutsutaan `NewGameView` -luokan metodia `show()`, jolle annetaan parametrina tyhjä nimimerkki (neljällä tähtimerkillä) sekä continue_textin väriksi harmaa väri. Tämän jälkeen `NewGameView` -luokka  kutsuu `Renderer` -luokan metodia `render_menu()`, joka renderöi uusipeli -näkymän ruudulle.

Seuraavaksi odotetaan käyttäjän syötettä tallennustiedon nimimerkiksi. Kunkin syötetyn tai pyyhityn kirjaimen jälkeen näkymä renderöidään uudelleen yllä kuvatulla tavalla. Continue_textin valinta aktivoidaan ja sen väri muutetaan valkoiseksi, kun käyttäjä on syöttänyt kaikki nimimerkin neljäkirjainta.

Tämän jälkeen luodaan uusi tallennustiedosta nimimerkin avulla `InformationService` -luokan `create_new_save(nickname)` -metodin avulla, joka edelleen kutsuu `save_repository` -oliota tekemään tallennuksen tietokantaan sekä palauttamaan tallennustiedon `Save` oliona.

Lopuksi kutsutaan käynnistäpeli -näkymän metodia `show_start_view()`.

### Lataapeli -näkymä

Lataapeli -näkymä aloitetaan kutsumulla `UI` -luokan metodia `show_load_game_view()`. Seuraava sekvenssikaavio esittää lataapeli -näkymän etenemisen:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-load.png" width="1000">

Aluksi pyydetään `InformationService` -luokkaa hakemaan ja järjestämään 8 ensimmäista tallennusoliota parhaimman etenemisen perusteella. Tämä tapahtuu metodilla `list_saves(8)`, joka edelleen kutsuu `save_repository` -olion metodin `find_and_sort_saves(8)` avulla hakemaan tulokset tietokannasta. Tuloksena palautetaan lista `Save` olioita, jotka talletetaan muuttujaan `saves`. Seuraavaksi kutsutaan `LoadGameView` -luokan metodia `show()`, jolle annetaan parametrina aiemmin haetut tulokset. Tämän jälkeen `LoadGameView` -luokka erittelee tulokset ja kutsuu `Renderer` -luokan metodia `render_menu()`, joka lopulta renderöi lataapeli -näkymän ruudulle.

Kun lataapeli -näkymä on ruudulla, niin jäädään odottamaan käyttäjän syötettä. Käyttäjä valitsee haluamansa tallennuksen, jonka jälkeen kyseinen tallennustiedosto haetaan tietokannasta ja palautetaan takaisin `Save` oliona `InformationService` -luokan sekä `save_repository` -olion avulla.

Lopuksi kutsutaan käynnistäpeli -näkymän metodia `show_start_view()`.

### Asetusnäkymä

Asetusnäkymä aloitetaan kutsumulla `UI` -luokan metodia `show_setup_view()`. Asetusnäkymässä suoritetaan seuraavat toimenpiteet silmukassa, kunnes käyttäjä painaa `ESC` näppäintä, jolloin suoritus palaa takaisin Menunäkymään:

1. Renderöidään asetusnäkymä ruudulle `Renderer` -luokan metodilla `render_menu()`
2. Haetaan tieto siitä, onko musiikki sekä ääniefektit päällä `AudioService` -luokan metodilla `get_audio_information()`
3. Odotetaan käyttäjältä syötettä, joka kertoo halutaanko muuttaa musiikin vai ääniefektin tilaan.
4. Kytketään musiikki tai ääniefekti päällä tai pois päältä riippuen siitä, mikä aiempi tila oli kyseessä.

### Käynnistäpeli -näkymä

Käynnistäpeli -näkymä aloitetaan kutsumulla `UI` -luokan metodia `show_start_view()`. Seuraava sekvenssikaavio esittää lataapeli -näkymän etenemisen:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-start.png" width="1000">

Käynnistäpeli -näkymään voidaan päätyä uusipeli- tai lataapeli -näkymien kautta sekä lisäksi pelisession päättymisen jälkeen. Tästä syystä käynnistäpeli- näkymässä pyydetään aluksi `AudioService` -luokan metodia `play_music()` käynnistämään menunäkymän kappale. Kyseinen metodi ei tee mitään, mikäli menunäkymän kappale on jo käynnissä eli kyseinen musiikin uudelleen toistaminen aloitetaan vain, jos siirtyminen näkymään tapahtuu pelisession päättymisen jälkeen.

Seuraavaksi haetaan aktiivisen tallennustiedon edistymistieto `InformationService` -luokan metodilla `get_progress_information()`, joka edelleen hakee tiedon oman `Save` -attribuuttinsa metodilla `get_information()` ja palauttaa takaisin käyttöliittymään. Tämän jälkeen kutsutaan `StartView` -luokan metodia `show()`, jolle annetaan parametrina aiemmin haetut tulokset. Sitten `StartView` -luokka erittelee tulokset ja kutsuu `Renderer` -luokan metodia `render_menu()`, joka lopulta renderöi käynnistäpeli -näkymän ruudulle.

Kun käynnistäpeli -näkymä on ruudulla, niin jäädään odottamaan käyttäjän syötettä, jonka tarkoituksena saadaan tieto pelitasosta. Käyttäjä valitsee haluamansa tason, jonka jälkeen kyseinen tieto välitetään `GameService` -luokan metodille `start_gameloop(level)`. Tämä käynnistää peliloopin ja pelaaminen voi alkaa.

### Pelilooppi

Pelilooppi aloitetaan kutsumalla `GameService` -luokan metodia `start_gameloop(level)`, jossa level viittaa `Käynnistäpeli -näkymässä` valittuun tasoon. Seuraava sekvenssikaavio esittää peliloopin etenemisen:

<img src="https://github.com/TopiasHarjunpaa/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssi-pelilooppi.png" width="1000">

Pelaaminen aloitetaan alustamalla uusi `LevelService` -luokan olio. `GameService` -luokka on saanut jo alustamisen yhteydessä parametreikseen näytön mitat sekä `AudioService` -luokan olion. Tasonumero annetaan metodikutsussa. `LevelService` -luokka alustaa peliin liittyvät objektit luokan `Sprites` avulla. `Sprites` luo tasonumeron perusteella kyseiseen tasoon liittyvät objektit kuten lattian, esteet sekä pelihahmon.

Seuraavaksi käynnistetään pelilooppi, jossa suoritetaan seuraavat toimenpiteet, kunnes `LevelService` -olio ilmoittaa pelin päättyneen:

1. Ajastimen päivittäminen `clock.tick()`
2. Käyttäjätoimintojen tarkastaminen `check_events()`
3. Pelitilan tarkistaminen `LevelService` -olion `update()` -metodin avulla: 
    * metodi päivittää pelissä näytettävät objektit, ylläpitää pelitilannetta, laskee tasopisteitä sekä välittää tiedon pelin jatkumisesta `GameService` -luokalle.
    * lisäksi metodi kutsuu metodeja `player_is_alive()`, `handle_jump()` sekä `handle_goal()`, jotka tarkastavat törmäyksiä eri objektien välillä sekä mahdollistavat oikeat toimenpiteet näiden perusteella.
4. Pelitilanteen renderöinti `Renderer` -luokan metodilla `render_game(level)`, jonka parametriksi annetaan `LevelService` -olio.

Pelilooppi päättyy joko pelaajan kuolemaan tai maaliin pääsemiseen. Lopuksi kutsutaan `UI` -luokan metodeita `show_finish_view()` tai `show_game_over_view()` lopputuloksesta riippuen. Nämä metodit aloittavat `Level Completed` tai `Game Over` -näkymän.

### Level Completed -näkymä

Level Completed -näkymä aloitetaan kutsumalla `UI` -luokan metodia `show_finish_view()`. Tämä tapahtuu silloin, Kun pelaaja on läpäissyt tason. Ensimmäiseksi pyydetään `AudioService` -luokkaa käynnistämään menunäkymän kappale. Seuraavaksi haetaan aktiivisen tallennustiedon edistymistieto `InformationService` -luokan metodilla `get_progress_information()`, joka edelleen hakee tiedon oman `Save` -attribuuttinsa metodilla `get_information()` ja palauttaa takaisin käyttöliittymään. Tason suorittaminen päivitetään tietokantaan, mikäli kyseistä tasoa ei ollut vielä aikaisemmin läpäisty.

Tämän jälkeen kutsutaan `FinishView` -luokan metodia `show()`, jolle annetaan parametrina aiemmin haetut tulokset sekä suoritetun tason numero. Sitten `FinishView` -luokka erittelee tulokset ja kutsuu `Renderer` -luokan metodia `render_menu()`, joka lopulta renderöi Level Completed -näkymän ruudulle.

Lopuksi odotetaan käyttäjän syötettä ja palataan takaisin menunäkymään tai käynnistäpeli -näkymään pelin jatkamista varten.

### Game Over -näkymä

Game Over -näkymä toimii samalla periaatteella kuin Level Completed -näkymä. Keskeisenä erona on ainoastaan se, että `InformationService` -luokan avulla haettua tietoa vertaillaan `LevelService` -luokan ylläpitämään edellisen pelisession edistymiseen, jonka avulla tietokanta päivitetään, mikäli edellisen pelisession tulos on tietokannassa olevaa tulosta parempi.
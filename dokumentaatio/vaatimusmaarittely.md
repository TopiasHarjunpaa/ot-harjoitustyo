# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen tasohyppelypeli, jonka esikuvana toimii [The Impossible Game](https://impossible.game/). Pelissä pelaajan tulee väistellä vastaan tulevia esteitä ja edetä mahdollisimman pitkälle.

## Toteutus

- Ohjelma toteutetaan Pythonilla ja Pygame-kirjaston avulla
- Tiedon tallennus tapahtuu SQLite-tietokannan avulla
- Ohjelman tulee toimia Linux-käyttöjärjestelmällä

## Käyttäjät

Pelissä on vain peruskäyttäjän rooli.

## Käyttöliittymäluonnos (Placeholder)

## Perusversion tarjoama toiminnallisuus

#### Aloitusvalikko

- Aloitusnäkymässä käyttäjälle näytetään pelin ennätykset
- Käyttäjä voi aloittaa uuden pelin:
    * Uuden pelin luominen tapahtuu omassa ikkunassa syöttämällä neljän merkin pituinen nimimerkki
- Käyttäjä voi jatkaa olemassa olevaa peliä:
    * Sovellus tallentaa kaikki uudet pelit nimimerkin perusteella tietokantaan
    * Pelin jatkaminen tapahtuu omassa ikkunassa, josta löytyy lista tallennetuista nimimerkeistä.

**Huom!** alustavan suunnitelman mukaan tarkoituksena oli luoda yksilöllinen käyttäjätunnus ja salasana, jonka avulla käyttäjä- ja pelitiedot talletetaan. Kyseessä on kuitenkin yksittäisellä laitteella oleva peli, joten tätä ei nähty tarpeelliseksi. Tästä syystä tiedot talletetaan ns. olemassa oleviin peleihin, jotka ovat kaikkien valittavissa / jatkettavissa.

*Aloitusvalikkon ulkoasu ja siirtymät toisiin valikoihin on melkein valmiita, mutta tietokantayhteyttä ei ole vielä muodostettu*

#### Pelivalikko

- Käyttäjä näkee listan tasoista
- Käyttäjä näkee oman nimimerkkinsä
- Käyttäjä näkee kussakin tasossa oman ennätyksensä
- Käyttäjä voi valita haluamansa tason (perusversiossa on vain yksi taso)
- Saavuttamattomat tasot ovat lukittuja
- Tason valinnan jälkeen peli käynnistyy
- Pelivalikosta voidaan palata takaisin aloitusvalikkoon

*Tällä hetkellä pelivalikon ulkoasu ja siirtymät ovat melkein valmiita. Tietokantayhteys keskeneräinen*

#### Pelinäkymä

- Yksinkertainen laatikkomainen grafiikka.
- Yksi taso, jossa pisteitä kertyy esimerkiksi piste per sekunti.
- Pelaajan *"kuolema"* käynnistää *Game Over -valikon*:
    * Tässä näytetään tason läpäisemisprosentti
    * Mahdollisuus palata takaisin pelivalikkoon ja aloittaa uudelleen
    * Mahdollisuus palata aloitusvalikkoon
- Tason läpäiseminen käynnistää *maalivalikon*:
    * Mahdollisuus palata takaisin pelivalikkoon (ja yrittää seuraavaa tasoa)
    * Mahdollisuus palata aloitusvalikkoon

*Tällä hetkellä peliin toteutettu yksi taso, jonka voi läpäistä. Valikoiden ulkoasu ja siirtymät ovat melkein valmiita. Tietokantayhteys keskeneräinen*

## Jatkokehitysideoita

Perusversion jälkeen mahdollisia kehitysideoita. Tuskin kuitenkaan realistista toteuttaa lähellekään kaikkia kurssin aikataulun puitteissa:

- Parannuksia pelin grafiikkaan:
    * Pelaajan hahmo ja muut objektit.
    * Tausta ja tasot.
- Äänet ja musiikki.
- Tasojen lisääminen
    * Ovat jo käyttöliittymässä olemassa, mutta toiminnallisuudet odottavat jatkokehitystä
    * Kun tason läpäisee, niin seuraavat tasot aukeavat.
- Asetusvalikko, jossa voisi säätää painikkeita, ääniä tai vaikka pelin vaikeusastetta (tavallinen, nopea, extra nopea jne...)
- Tallennettujen pelien suojaaminen salasanalla.
- Tallennettujen pelien poistaminen tai tallennettujen pelien määrän rajaaminen.
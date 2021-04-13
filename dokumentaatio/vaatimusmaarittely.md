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

- Aloitusnäkymässä käyttäjälle näytetään pelin ennätykset **[Done]**
- Käyttäjä voi aloittaa uuden pelin: **[Done]**
    * Uuden pelin luominen tapahtuu omassa ikkunassa syöttämällä neljän merkin pituinen nimimerkki
- Käyttäjä voi jatkaa olemassa olevaa peliä: **[Done]**
    * Sovellus tallentaa kaikki uudet pelit nimimerkin perusteella tietokantaan
    * Pelin jatkaminen tapahtuu omassa ikkunassa, josta löytyy lista tallennetuista nimimerkeistä.

**Huom!** alustavan suunnitelman mukaan tarkoituksena oli luoda yksilöllinen käyttäjätunnus ja salasana, jonka avulla käyttäjä- ja pelitiedot talletetaan. Kyseessä on kuitenkin yksittäisellä laitteella oleva peli, joten tätä ei nähty tarpeelliseksi. Tästä syystä tiedot talletetaan ns. olemassa oleviin peleihin, jotka ovat kaikkien valittavissa / jatkettavissa.

*Aloitusvalikko on pientä viilausta vailla valmis. Pieniä parannuksia voisivat olla mm:*
*- Nimimerkin korjaaminen ilman, että tarvitsee palata takaisin aloitussivulle*
*- Tallennettujen nimimerkkien poistaminen (näyttää tällä hetkellä vain 8 edistymisen mukaan parasta tallennusta)*

#### Pelivalikko

- Käyttäjä näkee listan tasoista **[Done]**
- Käyttäjä näkee oman nimimerkkinsä **[Done]**
- Käyttäjä näkee kussakin tasossa oman ennätyksensä **[Done]**
- Käyttäjä voi valita haluamansa tason (perusversiossa on vain yksi taso) **[Done]**
- Saavuttamattomat tasot ovat lukittuja **[Done]**
- Tason valinnan jälkeen peli käynnistyy **[Done]**
- Pelivalikosta voidaan palata takaisin aloitusvalikkoon **[Done]**

*Myös pelivalikko on pientä viilausta vailla valmis. Joitain muutoksia kuitenkin tarvitaan siinä vaiheessa, kun tasoja tullaan lisäämään peliin* 

#### Pelinäkymä

- Yksinkertainen laatikkomainen grafiikka **[Done]**
- Yksi taso, jossa pisteitä kertyy esimerkiksi piste per sekunti.
- Pelaajan *"kuolema"* käynnistää *Game Over -valikon*: **[Done]**
    * Tässä näytetään tason läpäisemisprosentti
    * Mahdollisuus palata takaisin pelivalikkoon ja aloittaa uudelleen
    * Mahdollisuus palata aloitusvalikkoon
- Tason läpäiseminen käynnistää *maalivalikon*: **[Done]**
    * Mahdollisuus palata takaisin pelivalikkoon (ja yrittää seuraavaa tasoa)
    * Mahdollisuus palata aloitusvalikkoon

*Tällä hetkellä peliin toteutettu yksi taso, jonka voi läpäistä. Valikoiden ulkoasu ja siirtymät ovat melkein valmiita, mutta itse pelissä on vielä reilusti parannettavaa.*

## Jatkokehitysideoita

Perusversion jälkeen mahdollisia kehitysideoita. Tuskin kuitenkaan realistista toteuttaa kaikkia kurssin aikataulun puitteissa:

- Parannuksia pelin pelattavuuteen (lähinnä siitä näkökulmasta, että pelaajat tykkäävät enemmän pelistä)
- Parannuksia pelin grafiikkaan:
    * Pelaajan hahmo ja muut objektit.
    * Tausta ja tasot.
- Äänet ja musiikki.
- Tasojen lisääminen (ovat käyttöliittymässä olemassa, mutta toiminnallisuudet odottavat jatkokehitystä)
- Asetusvalikko, jossa voisi säätää painikkeita, ääniä tai vaikka pelin vaikeusastetta (tavallinen, nopea, extra nopea jne...)
- Tallennettujen pelien suojaaminen salasanalla.
- Tallennettujen pelien poistaminen.
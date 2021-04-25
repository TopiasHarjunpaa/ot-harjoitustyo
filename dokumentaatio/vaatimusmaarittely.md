# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen tasohyppelypeli, jonka esikuvana toimii [The Impossible Game](https://impossible.game/). Pelissä pelaajan tulee väistellä vastaan tulevia esteitä ja edetä mahdollisimman pitkälle.

## Toteutus

- Ohjelma toteutetaan Pythonilla ja Pygame-kirjaston avulla
- Tiedon tallennus tapahtuu SQLite-tietokannan avulla
- Ohjelman tulee toimia Linux-käyttöjärjestelmällä

## Käyttäjät

Pelissä on vain peruskäyttäjän rooli.

## Perusversion tarjoama toiminnallisuus

### Aloitusvalikko

#### Perustoiminnallisuus

- Aloitusnäkymässä käyttäjälle näytetään pelin ennätykset **[Done]**
- Käyttäjä voi aloittaa uuden pelin: **[Done]**
    * Uuden pelin luominen tapahtuu omassa ikkunassa syöttämällä neljän merkin pituinen nimimerkki **[Done]**
    * Nimimerkkiä voi muuttaa ilman, että tarvitsee palata takaisin aloitussivulle ja aloittaa uudestaan **[Done]**
- Käyttäjä voi jatkaa olemassa olevaa peliä: **[Done]**
    * Sovellus tallentaa kaikki uudet pelit nimimerkin perusteella tietokantaan **[Done]**
    * Pelin jatkaminen tapahtuu omassa ikkunassa, josta löytyy lista tallennetuista nimimerkeistä **[Done]**

#### Jatkokehitysideoita

- Käyttäjät pystyvät poistaa tallennettuja nimimerkkejä (pelejä) **[]**
- Visuaaliset parannukset (parempi taustakuva yms.) **[]**  
- Asetusvalikko, jossa voisi säätää painikkeita, ääniä tai vaikka pelin vaikeusastetta (tavallinen, nopea, extra nopea jne...) **[]** 

### Pelivalikko

#### Perustoiminnallisuus

- Käyttäjä näkee listan tasoista **[Done]**
- Käyttäjä näkee oman nimimerkkinsä **[Done]**
- Käyttäjä näkee kussakin tasossa oman ennätyksensä **[Done]**
- Käyttäjä voi valita haluamansa tason **[Done]**
- Saavuttamattomat tasot ovat lukittuja **[Done]**
- Tason valinnan jälkeen peli käynnistyy **[Done]**
- Pelivalikosta voidaan palata takaisin aloitusvalikkoon **[Done]**

### Pelinäkymä

#### Perustoiminnallisuus

- Yksinkertainen laatikkomainen grafiikka **[Done]**
- Pisteiden laskeminen pelin edetessä (matkaa maaliin kuvataan prosentteina) **[Done]**
- Pelissä on neljä erilaista tasoa **[Done]**
- Pelaajan *"kuolema"* käynnistää *Game Over -valikon*: **[Done]**
    * Tässä näytetään tason läpäisemisprosentti **[Done]**
    * Mahdollisuus palata takaisin pelivalikkoon ja aloittaa uudelleen **[Done]**
    * Mahdollisuus palata aloitusvalikkoon **[Done]**
- Tason läpäiseminen käynnistää *maalivalikon*: **[Done]**
    * Mahdollisuus palata takaisin pelivalikkoon (ja yrittää seuraavaa tasoa) **[Done]**
    * Mahdollisuus palata aloitusvalikkoon **[Done]**

#### Jatkokehitysideoita

Perusversion jälkeen mahdollisia kehitysideoita. Tuskin kuitenkaan realistista toteuttaa kaikkia kurssin aikataulun puitteissa:

- Parannuksia pelin pelattavuuteen **[]** 
- Parannuksia pelin grafiikkaan **[]** 
    * Pelaajan hahmo ja muut objektit **[]** 
    * Tausta **[]** 
- Äänet ja musiikki **[Done]** 
- Useita tasoja **[Done]**
# Vaatimusmäärittely

TODO:t ennen lopullista palautusta:

1. Tee TOP3 records paremmin.
2. Siisti hieman progress informaatiota.
3. Tee puuttuvat testi.
4. Tee puuttuvat docstringit.
5. Lisää ympäristömuuttujat
6. Päivitä taustakuvat ja lisää jokaiselle maalle oma tausta.
7. Tarkasta koodi (tyylitarkistus, testit sekä visuaalinen tsekki)

Kun kaikki toiminnallisuudet yllä ovat valmiita:

1. Päivitä vaatimusmäärittely
2. Päivitä asennusohje ja kuvankaappaukset (lisää puuttuva setup)
3. Päivitä lopullinen luokka ja pakkauskaavio
4. Päivitä arkkitehtuurikuvaus (puuttuvia osioita)
5. Luo testausdokumentti.
6. Tsekkaa tuntikirjanpito ja tarkista tuntien summat.
7. Tarkasta tarvitseeko README lisätä jotain.
8. Lue vielä kertaalleen arvosteluperusteet.
9. Luo uusi release ja lisää linkki sekä README ja käyttöohje.
10. Poista nämä ja tee viimeinen push.
11. Sulje issue.

DEADLINE: su 16.5

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
    * Tausta **[Edistetty]** *(vaatii vielä parantamista)* 
- Äänet ja musiikki **[Done]** 
- Useita tasoja **[Done]**
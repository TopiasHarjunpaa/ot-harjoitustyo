# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen tasohyppelypeli, jonka esikuvana toimii [The Impossible Game](https://impossible.game/). Pelissä pelaajan tulee väistellä vastaan tulevia esteitä ja edetä mahdollisimman pitkälle.

Pelissä on neljä tasoa ja pelaajan tehtävänä läpäistä yksi kerrallaan. Aluksi vain ensimmäinen taso on auki ja kunkin tason läpäiseminen avaa mahdollisuuden yrittää seuraavaa tasoa. Pelin läpäisemiseksi vaaditaan `400% progress` eli kukin kenttä on läpäistävä `100%` pisteillä.

## Toteutus

- Ohjelma toteutetaan Pythonilla ja Pygame-kirjaston avulla
- Tiedon tallennus tapahtuu SQLite-tietokannan avulla
- Ohjelman tulee toimia Linux-käyttöjärjestelmällä

## Käyttäjät

Pelissä on vain peruskäyttäjän rooli.

## Perusversion tarjoama toiminnallisuus

### Aloitusvalikko

- Aloitusnäkymässä käyttäjälle näytetään pelin 3 parasta **[Done]**
- Käyttäjä voi aloittaa uuden pelin: **[Done]**
    * Uuden pelin luominen tapahtuu omassa ikkunassa syöttämällä neljän merkin pituinen nimimerkki **[Done]**
    * Nimimerkkiä voi muuttaa ilman, että tarvitsee palata takaisin aloitussivulle ja aloittaa uudestaan **[Done]**
- Käyttäjä voi jatkaa olemassa olevaa peliä: **[Done]**
    * Sovellus tallentaa kaikki uudet pelit nimimerkin perusteella tietokantaan **[Done]**
    * Pelin jatkaminen tapahtuu omassa ikkunassa, josta löytyy lista tallennetuista nimimerkeistä **[Done]**
- Pelaaja voi säätää pelin asetuksista musiikin sekä ääniefektit pois päältä tai takaisin päälle **[Done]** 


### Pelivalikko

- Käyttäjä näkee listan tasoista **[Done]**
- Käyttäjä näkee oman nimimerkkinsä **[Done]**
- Käyttäjä näkee kussakin tasossa oman ennätyksensä **[Done]**
- Käyttäjä voi valita haluamansa tason **[Done]**
- Saavuttamattomat tasot ovat lukittuja **[Done]**
- Tason valinnan jälkeen peli käynnistyy **[Done]**
- Pelivalikosta voidaan palata takaisin aloitusvalikkoon **[Done]**

### Pelinäkymä

- Yksinkertainen laatikkomainen grafiikka (pelaaja sekä esteet) **[Done]**
- Pisteiden laskeminen pelin edetessä (matkaa maaliin kuvataan prosentteina) **[Done]**
- Pelissä on neljä erilaista tasoa **[Done]**
- Pelaajan *"kuolema"* käynnistää *Game Over -valikon*: **[Done]**
    * Tässä näytetään tason läpäisemisprosentti **[Done]**
    * Mahdollisuus palata takaisin pelivalikkoon ja aloittaa uudelleen **[Done]**
    * Mahdollisuus palata takaisin aloitusvalikkoon **[Done]**
- Tason läpäiseminen käynnistää *maalivalikon*: **[Done]**
    * Mahdollisuus palata takaisin pelivalikkoon (ja siirtyä yrittämään seuraavaa tasoa) **[Done]**
    * Mahdollisuus palata aloitusvalikkoon **[Done]**
- Jokaisella tasolla on oma taustakuva **[Done]**
- Kussakin tasossa hahmon nopeus kasvaa **[Done]**
- Pelissä on taustamusiikki sekä ääniefektit mm. hyppäämiseen sekä kuolemaan **[Done]**

### Jatkokehitysideoita (ei toteuteta kurssin puitteissa)

- Käyttäjät pystyvät poistamaan tallennettuja nimimerkkejä
- Animoidut hahmot ja esteet
- Pelitasojen lisääminen ja sekä lisää erikoisuuksia kuhunkin tasoon
- Hyppytoiminnallisuuden parantaminen, kun käytettävissä oleva näytön resoluutio on eri suuri kuin 1920 x 1080.
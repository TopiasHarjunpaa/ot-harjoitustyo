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

## Perusversion tarjouma toiminnallisuus

#### Aloitusvalikko

- Aloitusnäkymässä käyttäjälle näytetään pelin ennätykset
- Käyttäjä voi aloittaa uuden pelin:
    * Uuden pelin luominen tapahtuu syöttämällä käyttäjätunnus (tai nimimerkki)
    * Samaa käyttäjätunnusta ei voi käyttää.
- Käyttäjä voi jatkaa olemassa olevaa peliä:
    * Sovellus tallentaa kaikki uudet pelit käyttäjätunnuksen mukaan.
    * Käyttäjä voi jatkaa olemassa olevaa peliä valitsemalla tallennustiedoston käyttäjätunnuksen perusteella.

Huom. alustavan suunnitelman mukaan tarkoituksena oli luoda yksilöllinen käyttäjätunnus ja salasana, jonka avulla käyttäjä tiedot talletetaan. Kyseessä on kuitenkin yksittäisellä laitteella oleva peli, joten tätä ei nähty tarpeelliseksi. Tästä syystä tiedot talletetaan ns. olemassa oleviin peleihin, jotka ovat kaikkien valittavissa / jatkettavissa. Myöhemmin voidaan selvittää nähdäänkö tarpeelliseksi lisätä ominaisuutta, jossa käyttäjä voi suojata olemassa olevan pelinsä salasanalla.

Tällä hetkellä aloitusvalikon toteutusta vastaa hieman harhaanjohtavasti kirjautumisikkuna, josta pääsee eteenpäin painamalla "l" painiketta. Toisin sanoen aloitusvalikon toiminnallisuutta ei ole juurikaan vielä toteutettu.

#### Pelivalikko

- Käyttäjä näkee valitussa pelissä olevan pistetilanteen
- Käyttäjä voi valita haluamansa tason (perusversiossa on vain yksi taso)
- Tason valinnan jälkeen peli käynnistyy
- Pelivalikosta voidaan palata takaisin aloitusvalikkoon

Tällä hetkellä pelivalikon toteutusta vastaa käynnistysikkuna, josta pääsee käynnistämään pelin painamalla "s" painiketta. Tätäkään toiminnallisuutta ei siis ole juurikaan toteutettu.

#### Pelinäkymä

- Yksinkertainen laatikkomainen grafiikka.
- Yksi taso, jossa pisteitä kertyy esimerkiksi piste per sekunti.
- Pelaajan "kuolema" käynnistää siirtymävalikon:
    * Siirtymävalikosta voi aloittaa tason uudelleen tai palata takaisin pelivalikkoon.
- Tason läpäiseminen käynnistää maalivalikon:
    * Maalivalikossa näytetään tason läpäisemisestä saadut pisteet.
    * Maalivalikosta voidaan palata takaisin pelivalikkoon.

Tällä hetkellä peliin toteutettu yksi taso, jonka voi läpäistä. Myös siirtymävalikot ovat olemassa, mutta niiden sisältö ja siirtymät eivät ole vielä valmiita.

## Jatkokehitysideoita

Perusversion jälkeen mahdollisia kehitysideoita. Tuskin kuitenkaan realistista toteuttaa lähellekään kaikkia kurssin aikataulun puitteissa:

- Parannuksia pelin grafiikkaan:
    * Pelaajan hahmo ja muut objektit
    * Tausta ja tasot
- Äänet ja musiikki
- Tasojen lisääminen
    * Uudessa pelissä voisi olla vain yksi taso auki ja muut lukittuina
    * Kun tason läpäisee, niin seuraavat tasot aukeavat
- Lisäpisteiden keräämisen mahdollisuus tason suorittamisen yhteydessä
- Asetusvalikko, jossa voisi säätää painikkeita, ääniä tai vaikka pelin vaikeusastetta (tavallinen, nopea, extra nopea jne...)
# Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovellus on yksinkertainen tasohyppelypeli, jonka esikuvana toimii [The Impossible Game](https://impossible.game/). Pelissä pelaajan tulee väistellä vastaan tulevia esteitä ja edetä mahdollisimman pitkällä.

### Toteutus

- Ohjelma toteutetaan Pythonilla ja Pygame -kirjastolla
- Tiedon tallennus tapahtuu paikalliseen tietokantaan (sqlite)
- Ohjelman tulee toimia Linux-käyttöjärjestelmällä

### Käyttäjät

Pelissä on vain peruskäyttäjän rooli.

### Käyttöliittymäluonnos

Placeholder

### Perusversion tarjouma toiminnallisuus

##### Ennen kirjautumista

- Käyttäjä voi luoda järjelmään käyttäjätunnuksen
- Käyttäjä voi kirjautua järjestelmään
- Käyttäjä näkee tilaston pelin tulosennätyksistä

##### Kirjautumisen jälkeen

- Käyttäjä näkee tulosennätysten lisäksi myös henkilökohtaisen ennätyksen
- Käyttäjä voi aloittaa uuden pelin
- Käyttäjä voi kirjautua ulos järjestelmästä

##### Pelin perusversio

- Yksinkertainen laatikkomainen grafiikka
- Yksi taso, jossa pisteitä kertyy esimerkiksi piste per sekunti

### Jatkokehitysideoita
Perusversion jälkeen mahdollisia kehitysideoita. Tuskin kuitenkaan realistista toteuttaa lähellekään kaikkia kurssin aikataulun puitteissa:

- Parannuksia pelin grafiikkaan:
    * Pelaajan hahmo ja muut objektit
    * Tausta ja tasot
- Äänet ja musiikki
- Mahdollisuus säätää vaikeusastetta
- Enemmän tasoja
- Omien tasojen luominen
- Tason loppuvastus
- Moninpeliominaisuus
- Tason läpäisemisen jälkeen mahdollisuus jatkaa seuraavalla kerralla etenemistä
- Karttanäkymä, johon on merkattu kaikki tasot (saavuttamattomat tasot ovat lukittuja)
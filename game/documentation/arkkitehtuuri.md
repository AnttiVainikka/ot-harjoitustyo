# Arkkitehtuuri

## Rakenne
![Rakenne- ja luokkakaavio](kaavio.jpg)
Kuvassa näkyy src-hakemistossa olevat alihakemistot ja niiden sisällöt sekä tiedosto main_code.py, joka aloittaa pelin suorituksen. Henkilöiden tekemiseen ja toimintaan liittyvät luokat löytyvät Classes-hakemistosta. Lisäksi on erillinen Sprites-hakemisto, missä on tarvittavat kuvat henkilöille sekä taustoille. StartGame-hakemistossa on pelin aloitukseen tarvittavat tiedostot ja UI-hakemistosta löytyy käyttöliittymään liittyvät tiedostot. Nuolet näyttävät, mitkä hakemistot ja tiedostot ovat liitoksissa mihin.

## Sovelluslogiikka
![Rakenne- ja luokkakaavio](kaavio.jpg)
Edellisestä kuvasta voimme myös nähdä sovelluslogiikan numeroitujen nuolien perusteella:
1.  main_code.py-tiedosto saa StartGame:n tiedostoilta itselleen kartan, pelattavat hahmot sekä viholliset.
2.  main_code.py-tiedosto aktivoi kartan sisältävän start- eli aloitusalueen, johon se sisältää hahmot ja viholliset.
3.  Start alue alkaa pyörittämään area.py:n koodia, jolloin pelaaminen voidaan aloittaa nuolinäppäimillä hahmoa liikuttamalla.
4.
- Kun alueesta siirrytään toiseen, niin area.py vie hahmot ja viholliset seuraavaan alueeseen ja alkaa pyörittämään sen koodia.
- area.py käyttää move.py-tiedostoa rekisteröimään pelaajan antamat liikkumiskomennot.
- Kun pelaata törmää viholliseen, niin koodi siirtyy battle.py-tiedostoon, jossa pelaaja hallinnoi taistelua vihollisia vastaan numeronäppäimillä action.py-tiedostoa käyttäen ja piirtämällä tarvittavat tiedot render.py tiedostolla.
- Kun taistelu on voitettu, niin siirrytään takaisin area.py:n koodiin siihen, missä viholliseen törmättiin, mutta vihollinen on poistettu alueesta. Vaihtoehtoisesti taistelu hävitään ja peli loppuu.
5.
- Pelaaja löytää main_code.py:n määrittämän boss-huoneen.
- Pelaaja kävelee boss-vihollisen luo ja aloittaa taistelun sen kanssa.
6.  Pelaaja voittaa boss-vihollisen ja area.py piirtää voittoruudun render.py:n avulla ja odottaa pelaajan lopettavan pelin sulkemalla pygamen ikkunan.

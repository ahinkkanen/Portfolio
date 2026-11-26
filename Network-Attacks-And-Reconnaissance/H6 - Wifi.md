# h6 Wifi


## a) Tutustu wifi challenge lab 2.1 harjoitus ympäristöön ja käytä tarvittaessa hyväksesi jo olemassa olevia ohjeita.

### Introduction

Tehtävän aloitin Käynnistämällä harjoitusympäristö virtuaalikoneen. WiFiChallenge sivustolta ensimmäinen harjoitus oli nimeltään ````Introduction````. Tehtävänanto oli selvittää tiedoston sisältö, jonka poluksi oli annettu ````/root/flag.txt````. Näkymä sivustolla ````00. What is the contents of the file /root/flag.txt on the VM?````. 

Tehtävän aloitin tarkastamalla, millä käyttäjällä olen kirjautuneena sisään. Tarkastin tämän komennolla ````whoami````. Seuraavaksi tarkoitus oli lähteä liikkumaan hakemistopuussa ylöspäin aina juurihakemistoon saakka, jossa on ````root```` -kansio. Siirryin juurihakemistossa ````root```` -kansioon ja sieltä löytyi ````flag.txt```` -tekstitiedosto. Tiedoston sisällön tulostin komentoriville ````cat```` -komennolla. Lippu löytyi ````flag.txt```` -tekstitiedostosta.

````
flag{2162ae75cdefc5f731dfed4efa8b92743d1fb556}
````

<img width="2486" height="1562" alt="image" src="https://github.com/user-attachments/assets/41a73dc9-9a6f-4e89-82b8-21922000ad61" />

Löydetyn lipun olin jo syöttänyt ````WiFiChallenge```` -sivustolle aiemmin, joten siksi näkymä oli tällä kertaa tämä. Kuitenkin lippu palautettiin onnistuneesti. 

<img width="2798" height="1530" alt="image" src="https://github.com/user-attachments/assets/05225024-862c-4532-8887-5850dce1b19b" />


### Recon

#### 01. What is the channel that the wifi-global Access Point is currently using?

Seuraavana tehtäväkseni otin järjestyksessä seuraavan tehtävän ````Recon```` -osioista nimeltään ````01. What is the channel that the wifi-global Access Point is currently using````. Aloitin luomalla tuleville tehtäville oman kansion nimeltä ````challenges````. Siirryin kansioon ja tarkastin komennolla ````iwconfig```` verkkokortit, joita virtuaaliympäristössä oli. Seuraavaksi kansion sisällä käynnistin ohjelman ````airmon-ng```` komennolla ````sudo airmon-ng start wlan0````.

<img width="1190" height="204" alt="image" src="https://github.com/user-attachments/assets/f8800006-ba0b-45b1-a740-587eb12e422e" />


<img width="2624" height="1374" alt="image" src="https://github.com/user-attachments/assets/53e6b9b0-790a-4698-876d-50335a263703" />

####

Seuraavaksi käynnistin ````airodump-ng````, jotta voin tarkastella saamaani liikenttä. Tämän käynnistin komennolla ````sudo airodump-ng wlan0mon -w ~/challenges/scan --manufacturer --wps --band abg````. Komentoriville ilmestyi liikennettä. Täältä silmään osui tehtävässä mainittu ````wifi-global```` Access Point ja sen kanava joka oli ````44````. 

<img width="2642" height="1280" alt="image" src="https://github.com/user-attachments/assets/899588c1-223f-4632-b8cb-6f83b522b24e" />

####

Puhtaasta mielenkiinnosta tahdoin vielä avata tiedoston ````WireShark```` -ohjelmaan, jotta voin tarkastaa näkeekö saman vastauksen myös sieltä. Hetkellisen tutkimisen jälkeen en kuitenkaan onnistunut löytämään samaa vastausta täältä.

<img width="1266" height="138" alt="image" src="https://github.com/user-attachments/assets/4d081751-8d49-4325-8ef0-9c38d11325d5" />


<img width="2034" height="1454" alt="image" src="https://github.com/user-attachments/assets/75a99517-3750-49d8-8a27-425ba00e4a1b" />

####

Palautin ````WiFiChallenges```` -sivustolle tehtävän palautukseen löytämäni vastauksen ````44```` ja se oli oikein.

<img width="2880" height="1534" alt="image" src="https://github.com/user-attachments/assets/bfbee0ec-1b94-484c-9456-d018e668a176" />

####

#### 02. What is the MAC of the wifi-IT client?


Tehtävää varten tarkastelin aiempaa näkymää, josta tein nopean olettaman, että haettu vastaus olisi ````wifi-IT```` kohdasta ````BSSID````. Kuvan perusteella se oli ````F0:9F:C2:1A:CA:25````. 

<img width="2642" height="1358" alt="image" src="https://github.com/user-attachments/assets/3e6f3531-35a2-4e27-8b8d-80d1d94c1f12" />

####

````
F0:9F:C2:1A:CA:25
````

####

Testasin syöttää vastausta harjoitukseen tarkastukseen, mutta se olikin väärin ja piti aloittaa tutkiminen erinäkökulmista. 

<img width="1100" height="1038" alt="image" src="https://github.com/user-attachments/assets/31644ac9-b3ab-40b9-b64a-23243e1e047b" />


####

Katsoin tässä kohtaa taas apua walktrough kohdasta ja syötin komennon ````sudo airodump-ng wlan0mon -w ~/challenges/scanc11 --manufacturer --wps -c11````. Tämä avasi uuden luettelon, josta selvisi juuri tämän ````wifi-IT````:n asiakas, joka on ````10:F9:6F:AC:53:52````. 

<img width="2880" height="1630" alt="image" src="https://github.com/user-attachments/assets/87d85019-61b0-4fdc-8038-e1942e87c788" />

Syötin alla olevan ````MAC-osoitteen```` tarkastukseen ````WiFiChallenges```` -sivustolla ja se oli oikein.

````
10:F9:6F:AC:53:52
````

####

<img width="986" height="1300" alt="image" src="https://github.com/user-attachments/assets/311fea54-f8d3-44a1-a957-3dd53130decc" />


#### 03. What is the probe of 78:C1:A7:BF:72:46?

Lähdin tarkastelemaan aiemmin käytetyn komennon ````sudo airodump-ng wlan0mon -w ~/challenges/scan --manufacturer --wps --band abg```` tulostetta ja sieltä alhaalta asiakkaiden näkymästä löytyi ````Probes```` -valikosta vastaus ````wifi-offices,Jason````. Syötin tuon aluksi ````WiFiChallenges```` -sivustolle, mutta se palautti virheen. Tämän jälkeen testasin vastaukselle eri muotoa ````wifi-offices```` ja se toimi.

<img width="2284" height="1390" alt="image" src="https://github.com/user-attachments/assets/b57de0c6-14ad-4065-97a9-e7b7b030ddc9" />


<img width="1010" height="1474" alt="image" src="https://github.com/user-attachments/assets/eaa08ba8-d212-414d-8c00-347e5796a9ed" />


## b) Kirjoita raportti siitä mitä opit ja mitkä asia yllättivät sinut kun tutustuit harjoitukseen.


Harjoituksessa opin, kuinka paljon tietoa langattomasta verkosta saa selville pelkästään kuuntelemalla liikennettä. Verkkoon ei tarvinnut kirjautua, mutta silti sain selville esimerkiksi Access Pointin kanavan ja asiakaslaitteiden MAC-osoitteet. Yllättävää oli, että tein ````wifi-IT```` -tehtävässä aluksi väärän oletuksen ja vastasin Access Pointin osoitteen asiakaslaitteen sijasta. Tästä opin, että Access Point ja asiakaslaite pitää osata erottaa toisistaan. Toinen yllätys oli, että asiakas löytyi vasta, kun rajasin skannauksen yhteen kanavaan. Pelkkä yleinen skannaus ei siis aina näytä kaikkea. Eniten minua yllätti kuitenkin ````Probes```` -sarake, koska laitteen aiemmin käyttämät verkot näkyivät, vaikka laite ei ollut yhteydessä mihinkään. Harjoitus oli mielestäni hyvä tapa nähdä, mitä langattomassa liikenteessä oikeasti näkyy ja miten sitä tutkitaan.


## c) Miten suhtautumisesi WLanin turvallisuuteen muuttui sen jälkeen kun teit harjoitukset?

Aiemmin ajattelin WLANin turvallisuuden olevan lähinnä salasanan varassa. Harjoituksen jälkeen ymmärsin, että langaton verkko on aina periaatteessa kaikkien kuunneltavissa, koska radioaaltoja ei voi rajata seinien sisälle. Jo ennen salauksen murtamista voi saada selville verkkojen nimiä, laitteita ja jopa laitteiden aiemmin käyttämiä verkkoja. Siksi turvallisuutta ei kannata perustaa siihen, että verkon tietoja yritetään pitää piilossa. Yleisten käytäntöjen mukaan tärkeää on käyttää vahvaa salausta, pitkää salasanaa ja erottaa vieraiden verkko omasta verkosta. Myös omien laitteiden vanhat tallennetut verkot kannattaa poistaa, ettei laite paljasta niitä. Jatkossa suhtaudun WLANiin varovaisemmin, varsinkin julkisissa verkoissa. Oletan nyt, että osa laitteen ja verkon tiedoista on aina jonkun nähtävillä.

## Lähteet:

* Claude Sonnet 5.5 Low
* https://terokarvinen.com/verkkoon-tunkeutuminen-ja-tiedustelu/
* https://lab.wifichallenge.com/challenges
* https://r4ulcl.com/posts/walkthrough-wifichallenge-lab-2.0/#04-what-is-the-essid-of-the-hidden-ap-mac-f09fc26a88

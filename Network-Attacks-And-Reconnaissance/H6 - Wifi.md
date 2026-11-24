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

Seuraavana tehtäväkseni otin järjestyksessä seuraavan tehtävän ````Recon```` -osioista nimeltään ````01. What is the channel that the wifi global Access Point is currently using````. Aloitin luomalla tuleville tehtäville oman kansion nimeltä ````challenges````. Siirryin kansioon ja tarkastin komennolla ````iwconfig```` siellä käynnistin ohjelman ````airmon-ng```` komennolla ````sudo airmon-ng start wlan0

<img width="1190" height="204" alt="image" src="https://github.com/user-attachments/assets/f8800006-ba0b-45b1-a740-587eb12e422e" />


<img width="2624" height="1374" alt="image" src="https://github.com/user-attachments/assets/53e6b9b0-790a-4698-876d-50335a263703" />


<img width="2642" height="1280" alt="image" src="https://github.com/user-attachments/assets/899588c1-223f-4632-b8cb-6f83b522b24e" />


<img width="2034" height="1454" alt="image" src="https://github.com/user-attachments/assets/75a99517-3750-49d8-8a27-425ba00e4a1b" />


<img width="2880" height="1534" alt="image" src="https://github.com/user-attachments/assets/bfbee0ec-1b94-484c-9456-d018e668a176" />


## b) Kirjoita raportti siitä mitä opit ja mitkä asia yllättivät sinut kun tutustuit harjoitukseen.




## c) Miten suhtautumisesi WLanin turvallisuuteen muuttui sen jälkeen kun teit harjoitukset?


## Lähteet:

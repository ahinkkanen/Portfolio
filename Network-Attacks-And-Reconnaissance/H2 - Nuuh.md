# H2 Nuuh

## x) Lue ja tiivistä

* Karvinen 2025: Wireshark - Getting Started
  
  ````
  * Wireshark on tunnetuimpia ja johtavimpia verkkojen sniffaus työkalu
  * Lähtökohtaisesti konfiguraatiossa aina annetaan myös muidenkin, kuin "superusers" siepata liikennettä
  * Wireshark näyttää ennen jo liikeenteen sieppaamista, miltä verkkokorteilta löytyy aktiivista liikennettä
  * Sininen kalanevä vasemmassa yläkulmassa aloittaa liikenteen sieppaamisen
  * Punainen neliö lopettaa sieppaamisen
  * Siepattua liikennettä voi tarkastella jälkeenpäin ja sitä varten on erilaisia filttereitä, kuten dns, tls ja http
  ````
  
* Karvinen 2025: Network Interface Names on Linux

````
* Linuxissa verkkoliittymät ovat nimetty en --> Wired Ethernet, wl --> WLAN & lo --> Loopback (localhost)
* Nimet tulevat systemd:ltä
* Verkkoliittymät voivat tarkastaa Linux terminaalissa komennoilla "ip a" ja "ip route"
````

## a) Linux.

Minulla on käytössä natiiviksi asennettu Parrot OS, jolla teen kurssin tehtäviä. Tarvittaessa voin käynnistää Windowsin, josta voin käynnistää virtuaali Kali Linuxin. Parrot OS on debian pohjainen Linux distro.


## b) Ei voi kalastaa.

Osoitukset, että kykenen katkaisemaan ja palauttamaan tietokoneeni verkkoyhteyde. Kuvat ovat alla.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5abe997e-82a4-49d7-8e4c-fc082143bcc6" />


<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/1099f6d0-bd4a-496c-a181-63dbf4ebacb4" />


## c) Wireshark.

Wireshark on valmiina asennettuna Parrot OS. Laitoin taustalle ````ICMP```` -protokollalla pyörivän ````ping```` -komennon pyörimään taustalle ja käynnistin Wiresharkin terminaalista komennolla ````sudo wireshark````. Seuraavaksi Wireshark ohjelma aukeaa ja sieltä valitsin verkkokortin, jolla lähin sieppaamaan liikennettä. Alimmasta kuvasta näkee sieppaamaani liikennettä, jossa ilmenee esimerkiksi taustalleni laittamaa ````ping```` -komentoa, joka ottaa yhteyttä jatkuvasti Cloudflaren DNS-palvelimeen. 


<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/ddd2f5f4-ef8c-4bc1-b10a-8085faa060b9" />

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/63bae561-8f3e-4efd-8a90-f290d9c32b7b" />

## d) Oikeesti TCP/IP.

Kuvasta ilmenee yksi valitsemani paketti.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/d9d3a703-e736-4e5c-9dfa-787e7af82b43" />






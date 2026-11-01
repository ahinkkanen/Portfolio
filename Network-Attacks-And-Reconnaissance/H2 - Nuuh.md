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

Kuvasta ilmenee yksi valitsemani paketti ja sen TCP/IP kerrokset laatikoituna.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/d9d3a703-e736-4e5c-9dfa-787e7af82b43" />

#### Tiedot:

````
* Sovelluskerros: Transport Layer Security, TLSvv1.3
* Kuljetuskerros: Transmission Control Protocol, Src Port: 25174, Dst Port: 443
* Internetkerros: Internet Protocol Version 4, Src: 192.168.1.103, Dst: 140.82.121.6
* Linkkikerros: Ethernet II, MAC-osoitteet
````

## e) Mitäs tuli surfattua?

Kaappaus on kohtalaisen lyhyt ja se sisältää yhteensä 283 pakettia. Kaappauksessa ilmenee, että ensimmäinen kone ottaa yhteyden DNS-palvelimeen ja tekee kyselyn, joka Googlen palvelimelle. Myös yhteys muodostetaan terokarvinen.com sivuun DNS-kyselyn kautta. En löytänyt mitään salaamatonta liikennettä siepatusta verkkoliikenteestä, kuten ````http```` -liikennettä. Valtaosa Liikenteestä oli salattua ````QUIC````- ja ````TLS```` liikennettä. Siepatussa liikenteessä ````192.168.122.7```` näyttää olevan jonkin käyttäjän kone, koska se ottaa aina yhteyttä eri palvelimiin.


## f) Vapaaehtoinen.

````-````


## g) Minkä merkkinen verkkokortti käyttäjällä on?

Pyrin ratkaisemaan tätä tutkimalla pakettien tietoja ja varsinkin käyttäjän laitteen tietoja (````192.168.122.7````). Tietoja tutkin Wiresharkista. Avasin ensimmäisen paketin ja sieltä tutkin linkkikerroksen tietoja. Täältä löytyi käyttäjän laitteen MAC-osoite, joten aloin sitä tarkastelemaan verkosta löytämällä työkalulla ````MACLookup````. Kuitenkaan tämä ei antanut valmistajaa minulle vaan esitti, että kyseessä olisi yksityinen osoite, eikä täten laitevalmistajaa ole saatavilla julkisesti. Pohdin tähän syyksi, että voiko kyseessä olla virtuaali tietokone vai onko vain laitevalmistaja saatu salattua osoitteen taakse.

#### Alla on kuvia tehtävästä
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/a5e18389-9769-4d6f-872b-3575768b26fe" />

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/dcf8ec4b-4341-4216-b2cc-704882738cf2" />


## h) Millä weppipalvelimella käyttäjä on surffaillut?

Käyttäjä on surffannut terokarvinen.com palvelimella. Tämä ilmenee DNS-kyselyistä. Toisiaan kuitenkin liikenne on TLS-salattua. Yritin käydä katsomassa onko löytämäni ````https://goatcounter.netlify.com/```` palvelin olemassa, mutta sieltä tuli kielteinen vastaus ja tutkittuani asiaa se taitaa vain olla terokarvinen.com palvelimeen integroitu kävijälaskuri. Sama kävi ````https://gc.zgo.at/```` kanssa.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5bbfec9a-d6d8-476c-8578-626f7edd94fa" />

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/6c3694b2-0dff-412a-b092-6be298927791" />

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/a9e92f78-b980-4654-b234-8ddf4ff29603" />


## i) Analyysi.

Aloitin sieppauksen käynnistämällä Wiresharkin ja sieltä valitsemalla verkkokortin, jolla siepata verkkoni läpi kulkevaa liikennettä. Tähän valitsin Wiresharkista WLAN-rajapinnaksi ````wlp98s0````. Kaappaukseni kesti 27 sekuntia ja sen ajan puitteissa paketteja kertyi yhteensä 5706. Sieppauksen aikana tarkoituksellisesti avasin Brave selaimella webbi osotteita, jotta sain liikennettä verkkoni sisällä kasvatettua. Avasin selaimessa terokarvinen.com, Haaga-Helian Moodlen ja YouTuben. Verkossani käyttämäni kone, jolla liikennettä sieppasin ja simuloin oli ````192.168.1.103````. Myös sieppauksessa ilmenee DNS-kyselyitä, jotka kulkevat minun itse hostaamna DNS-palvelimen läpi ````192.168.1.101````. Liikenteeni oli TLS-salattua ja siellä oli myös ARP-kyselyitä. Lisäksi QUIC-liikennettä oli. 

Kuvissa näkyy kun olen suodattanut filtteröimällä liikennettä eri komennoilla, kuten ````dns.flags.response == 0```` ja ````tls.handshake.type == 1````. Nämä näyttää mitä nimiä koneeni kysyi ja mihin palvelimiin on otettu yhteyttä.


<img width="1389" height="868" alt="image" src="https://github.com/user-attachments/assets/ae4f1c6f-a87c-4711-892d-420769689d39" />

<img width="1389" height="868" alt="image" src="https://github.com/user-attachments/assets/c1f139bc-e42b-4200-8e49-00df8367f7d9" />


## Lähteet:

* https://terokarvinen.com/wireshark-getting-started/
* https://terokarvinen.com/network-interface-linux/
* https://terokarvinen.com/verkkoon-tunkeutuminen-ja-tiedustelu/surfing-secure.pcap
* https://wireshark.com/how-to-use-wireshark/
* https://maclookup.app/

# H5 Labratakki


## a) Aja tunnilla esitetty ARP hyökkäys ja tutki, miten se toimii.

Tehtävän aloitin avaamalla ````Mininet```` -koneen ja alustin koneen harjoitusta varten ohjeiden mukaisesti. ````Mininet```` koneessa ajettiin alla oleva komento.

````
ryu-manager ryu.app.simple_switch_13
````

Viereen avasin ````PuTTY```` -ohjelman, jolla otin ````SSH```` -yhteyden myös ````Mininet```` -koneeseen, jotta voin ajaa ohella toisen komennon pyörimään. Komento alla.


````
sudo mn --topo single,3 --mac --switch ovsk --controller remote
````

Lopuksi vielä ajoin ````pingall```` -komennon mininetin sisällä, koska tämä varmisti, että yhteydet harjoitusta varten olevilla virtuaalikoneilla toimivat. 

### 
<img width="2834" height="1378" alt="image" src="https://github.com/user-attachments/assets/ef771ebe-9d3b-4884-82c0-db3faebfaa74" />

###

<img width="742" height="240" alt="image" src="https://github.com/user-attachments/assets/04f9db8c-5984-4674-884f-59a11a3f0271" />

###

Minulla tuli kuitenkin ````PuTTY:n```` kanssa ongelma ja en ollut huomannut mallista tähän vielä tässä vaiheessa korjausta niin vaihdoin kesken kaiken pois ````PuTTY:sta```` ja siirryin ````Kaliin````, josta otin SSH yhteyden ````Mininettiin````.

<img width="594" height="134" alt="image" src="https://github.com/user-attachments/assets/d80aaf04-6379-46f2-a05a-3ddaac3a6800" />


### Vaihdoin Kaliin, tein samat toimenpiteet ja testasin yhteyksien toimivuuden uudestaan.

<img width="912" height="326" alt="image" src="https://github.com/user-attachments/assets/32dc9cdc-765b-44ec-953e-b6535cd5f737" />

Seuraavaksi oli tarkoitus avata ````Node: h1```` pystyyn komennolla ````xterm h1````. Pieni terminaali aukesi ja se toimi.

<img width="426" height="62" alt="image" src="https://github.com/user-attachments/assets/629c50a5-98b6-40b8-b93d-c4ee718ff03e" />

###


<img width="1918" height="286" alt="image" src="https://github.com/user-attachments/assets/84fc0f75-ba39-4299-9026-29da757a972e" />


###

Kurkkasin komennolla ````arp -n```` taulukon, josta ilmeni ````ip````, ````verkkotyyppi```` ja ````MAC````.


<img width="726" height="140" alt="image" src="https://github.com/user-attachments/assets/44b95a97-3795-4d63-8971-1681a1fb71da" />

###

Seuraavaksi otettiin avattiin yhteys ````Node: h3```` terminaali näkymään samalla ````xterm h3```` -komennolla. ````h3```` koneen sisällä ajettiin komentoja tehtävää määrityksiä varten.

````
sysctl -w net.ipv4.ip_forward=1

iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --toport 22

tcpdump –i h3-eth0 –w arp-p.pcap &
````

<img width="1138" height="268" alt="image" src="https://github.com/user-attachments/assets/8a075d48-78bc-4b2a-94c9-9c4fc2ece8f0" />


###

Seuraavaksi lähdettiin WireSharkin avulla kuuntelemaan ````h1-eth0```` -verkkoa valitsemalla ````h3-eth0```` -liitäntä. WireShark avattiin komentoriviltä ````wireshark &```` -komennolla. Nopeasti huomasin kuitenkin, että siinä ei ollut vielä yhtään kaapattua liikennettä. 

<img width="1310" height="944" alt="image" src="https://github.com/user-attachments/assets/f40c3b80-90e2-488e-9338-6a75bebab4ce" />


Kävin vielä ````Node: h3```` sisällä määrittämässä yhden tärkeän komennon ````ARP-myrkytyksen```` sieppaamsita varten ````sshesame -port 22 -listen_address 0.0.0.0````. Avasin vielä uuden ````h3```` terminaalin ja sinne laitoin myrkytys skriptin pyörimään. 

<img width="736" height="162" alt="image" src="https://github.com/user-attachments/assets/ce495feb-cf1e-46f5-81b3-c1a76e096260" />

###

Seuraavaksi oli tarkoitus ottaa ````h1```` koneelta ````SSH```` -yhteys ````h2```` -koneeseen. Komennolla ````ssh h2````.


<img width="860" height="774" alt="image" src="https://github.com/user-attachments/assets/3ef1ca03-713a-48d8-b264-a51b85a6b06c" />

### 

Tämä varoitus vaati pienen toimenpiteen, jotta myrkytys saadaan lopulta onnistumaan. Tässä täytyi poistaa vanha ````SSH```` -avain komennolla ````ssh-keygen –R h2````. Sitten voimme ottaa uudelleen ````SSH```` -yhteyden ````h1```` -koneesta koneeseen ````h2````. Syötettyä tehtävän annon mukainen salasana eli ````salasana```` päästiin onnistuneesti sisään ````h2```` koneelle.


<img width="806" height="230" alt="image" src="https://github.com/user-attachments/assets/d36492b8-45b1-47d4-a18b-c62e55b825f1" />

Kääntöpuolena tehtävän todellinen tarkoitus ilmenee nyt ````h3```` -koneessa, koska sinne on ilmestnyt ````SSH```` -kirjautumistiedot. 

<img width="1856" height="394" alt="image" src="https://github.com/user-attachments/assets/d1d68cee-4875-4093-9e8a-8efa039c1760" />


### Yhteenveto

Tehtävässä havainnollisteettiin, kuinka ARP-myrkytys eli toisin sanoen Man In The Middle -hyökkäys konkreettisesti toimii. Tässä hyökkääjä lähettää verkkoon ns. vääriä viestejä, jotka saavat kaksi konetta luulemaan, että toisen osoite kuuluisikin hyökkääjälle. Tämän jälkeen koneiden välinen liikenne kulkeekin hyökkääjän kautta, vaikka ne luulevat puhuvansa suoraan toisilleen. Hyökkääjä kykenee näin lukemaan niiden liikenteen. Harjoituksessa yhteys meni hyökkääjän koneen kautta ja tämä sai talteen mm. salasanan.

## b) Samassa hakemistossa on myös ICMP Spoofing ja TCP Session Hijacking. Aja molemmat labrat läpi ja kerro, miten molemmat tekniikat toimivat.


### ICMP Spoofing

Labran aloitin ottamalla ````SSH```` -yhteyden ````Mininet```` -koneeseen. Seuraavaksi navigoin itseni oikeaan hakemistoon ````mininet@mininet-vm:~/lab/01-Network-Security-Lab/scripts$````. Sen jälkeen aloin noudattamaan GitHubista labran ajoon ohjeita. 

Kyseisen labran ohjeet löytyvät README.md osiosta repositoriossa:

````
https://github.com/ssam246/Network-Security-Lab/blob/main/README.md
````

Aluksi käynnistettiin ````Mininet```` -ympäristö.

````sudo python hub_topo.py````

Seuraavaksi käynnistin ````h1```` ja ajoin sinne käyntiin skriptin, joka tarkkailee ja tulostaa kaiken ICMP-liikenteen ja lähtevät echo-requestit sekä saapuvat echo-replyt.

````xterm h1````

````python sniff_icmp.py````

Lopuksi käynnistin toisen ikkunnan ````h2````, jossa käynnistin ````ICMP```` -protokollalla toimivan ````ping```` -komennon, joka lähetti jatkuvasti paketteja toiselle koneelle.

````xterm h2````

````ping 10.0.0.1````

<img width="2348" height="1364" alt="image" src="https://github.com/user-attachments/assets/1a3963f1-ce39-42f8-ba6c-214073b5e4c8" />

<img width="2284" height="1054" alt="image" src="https://github.com/user-attachments/assets/1c94ee64-4355-49f4-84ec-8446f8650c15" />

#### Toiminta ICMP Spoofing

Tässä labrassa Host 2 pingasi Host 1:tä ja Host 1:llä oli ajettu sniff_icmp.py, joka tarkkaili ja tulosti kaiken ICMP-liikenteen sekä lähtevät echo-requestit, että saapuvat echo-replyt omalta verkkoliitännältään. Tämä mallinsi sitä, että ICMP-paketit kulkevat verkossa ilman mitään todennusta ja kuka tahansa, joka näkee liikenteen tai pystyy lähettämään paketteja, voisi yhtä hyvin väärentää ICMP-viestin ja väittää sen tulevan toiselta koneelta, eikä vastaanottaja pystyisi sitä havaitsemaan.


### TCP Session Hijacking

<img width="2306" height="1260" alt="image" src="https://github.com/user-attachments/assets/9ce08018-fabf-407f-b24d-a44d50ea469f" />

#### Toiminta TCP Session Hijacking

Tässä labrassa mallinnetaan TCP-istunnon kaappaus, jossa Host 1 ja Host 2 keskustelivat normaalisti keskenään. Host 3 kuunteli tätä keskustelua sivusta ja näki siitä tunnistetiedot, joiden avulla yhteys tunnistetaan. Näiden tietojen avulla Host 3 pystyi lähettämään oman viestin niin, että se näytti tulevan suoraan Host 2:lta.































## c) Hakemistossa 02-SDN-DDos_Simulation tryout-kansiossa on työkalut, jotta voit ajaa TCP SYN-Flood-hyökkäyksen turvallisesti. Kirjoita, miten ajoit hyökkäyksen ja miten kyseinen hyökkäys toimii.





## Lähteet:

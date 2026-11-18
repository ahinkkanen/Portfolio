# H5 Labratakki


## a) Aja tunnilla esitetty ARP hyökkäys ja tutki, miten se toimii.

Tehtvän aloitin avaamalla ````Mininet```` -koneen ja alustin koneen harjopitusta varten ohjeiden mukaisesti. ````Mininet```` koneessa ajettiin alla oleva komento.

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


### Vaihdoin Kaliin ja testasin yhteyksien toimivuuden uudestaan.

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

Seuraavaksi lähdettiin WireSharkin avulla kuuntelemaan h1-eth0 verkkoa valitsemalla h3-eth0 liitäntä. WireShark avattiin komentoriviltä ````wireshark &```` -komennolla. Nopeasti huomasin kuitenkin, että siinä ei ollut vielä yhtään kaapattua liikennettä. 

<img width="1310" height="944" alt="image" src="https://github.com/user-attachments/assets/f40c3b80-90e2-488e-9338-6a75bebab4ce" />


Kävin vielä ````Node: h3```` sisällä määrittämässä yhden tärkeän komennon ````ARP-myrkytyksen```` sieppaamsita varten ````sshesame -port 22 -listen_address 0.0.0.0````. Avasin vielä uuden ````h3```` terminaalin ja sinne laitoin myrkytys skriptin pyörimään. 

<img width="736" height="162" alt="image" src="https://github.com/user-attachments/assets/ce495feb-cf1e-46f5-81b3-c1a76e096260" />

###

Seuraavaksi oli tarkoitus ottaa ````h1```` koneelta ````SSH```` -yhteys ````h2```` -koneeseen. Komennolla ````ssh h2````.


<img width="860" height="774" alt="image" src="https://github.com/user-attachments/assets/3ef1ca03-713a-48d8-b264-a51b85a6b06c" />



### 

<img width="1856" height="394" alt="image" src="https://github.com/user-attachments/assets/d1d68cee-4875-4093-9e8a-8efa039c1760" />






<img width="860" height="774" alt="image" src="https://github.com/user-attachments/assets/9fb97e92-9254-4378-9e5b-232be0f1cd90" />

## b) Samassa hakemistossa on myös ICMP Spoofing ja TCP Session Hijacking. Aja molemmat labrat läpi ja kerro, miten molemmat tekniikat toimivat.





## c) Hakemistossa 02-SDN-DDos_Simulation tryout-kansiossa on työkalut, jotta voit ajaa TCP SYN-Flood-hyökkäyksen turvallisesti. Kirjoita, miten ajoit hyökkäyksen ja miten kyseinen hyökkäys toimii.





## Lähteet:

# Raspberry Pi Palvelin

Halusin rakentaa itselleni yksityisyys edellä rakennettu kotipalvelin Raspberry Pi 4:n päälle. Tavoitteena on pitää oma verkkoliikenne ja henkilökohtainen data omassa hallinnassa sen sijaan, että ne kulkisivat jonkun toisen palveluntarjoajan pilvipalvelun kautta.

## Johdanto

Halusin kotiin pienen, jatkuvasti päällä olevan koneen, joka hoitaa asiat, jotka muuten antaisin ulkopuolisten palveluiden hoidettavaksi: DNS-suodatuksen, oman datan tallennuksen ja muiden projektieni keskuksen. Raspberry Pi 4 on edullinen, hiljainen ja kuluttaa vähän sähköä, joten se sopii hyvin vuorokauden ympäri käyvään kotilaboratorioon. Projekti antoi myös käytännön harjoitusta opiskelemistani asioista: Linux-ylläpidosta, tietoverkoista ja tietoturvasta.

[Kuva 1: Raspberry Pi 4 paikallaan kotona / laitteiston yleiskuva]

## Mitä palvelin tekee
Pi-hole estää mainokset ja seurantaosoitteet kaikilta kotiverkon laitteilta. Kaikki DNS-kyselyt kulkevat Quad9:n kautta. Se on yksityisyyttä painottava DNS-palvelu, joka estää myös tunnetut haitalliset verkkotunnukset.
Henkilökohtaisen datan tallennus. Paikallinen PostgreSQL-tietokanta, jolle annoin nimeksi "Data-ämpäri", pyörii Podman-kontissa. Siihen tallennetaan omaa dataa, esimerkiksi kuntodataa, omalle laitteistolle eikä palveluntarjoajan järjestelmiin. Pi:hin kytketty pieni OLED-näyttö kertoo järjestelmän sen hetkistä statistiikkaa. Näyttö käynnistyy automaattisesti käynnistyksen yhteydessä systemd-palveluna.

[Kuva 2: Pi-holen hallintapaneeli (piilota IP-osoitteet) tai OLED-näyttö toiminnassa]

## Hallinta

Hallitsen Raspberry Pi 4 palvelintani omalta pöytäkoneeltani ````ssh```` yli.

## Oppi:

Ensimmäisessä versiossa käytin useimpiin palveluihin Docker-kontteja. Törmäsin pitkäkestoisiin verkko-ongelmiin: Pi:n sisäänrakennetun verkkokortin ajurin (bcmgenet) ja Dockerin käyttämän bridge/NAT-kerroksen välillä oli ristiriitoja. Sen sijaan että olisin kasannut kiertotapoja päällekkäin, tein koko palvelimen uudelleen ja siirsin keskeiset palvelut natiiveihin asennuksiin. Esimerkiksi Pi-hole pyörii nyt suoraan käyttöjärjestelmässä.

Lopputulos on helpompi ymmärtää ja vianmääritys on helpompaa, koska liikkuvia osia on vähemmän. Niissä palveluissa, joissa kontit olivat järkevä ratkaisu, kuten tietokannassa, käytin Podmania.

## Lisä opit:
Verkko-ongelmien selvittäminen kerros kerrallaan, aina ajuritason käyttäytymiseen asti
Natiivin ja konteissa ajettavan palvelun valinta todellisten kompromissien perusteella, ei tottumuksen
Palveluiden luotettava ajaminen systemd:llä
Kotiverkon rakentaminen yksityisyys ja hallinta suunnittelutavoitteina
Alusta aloittaminen silloin, kun perusta on väärä, korjailun sijaan

## Tila:

Palvelin on tällä hetkellä päivittäisessä käytössä kotilaboratorioni selkärankana ja kasvaa, kun lisään uusia projekteja.

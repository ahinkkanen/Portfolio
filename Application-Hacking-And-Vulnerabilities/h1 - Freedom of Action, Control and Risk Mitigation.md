# h1 Freedom of Action, Control, and Risk Mitigation


## a) Basic Level


a1) What is included in the scope

* Kotini tietoverkko infrastruktuuriini kuuluu ISP-reititin, joka mahdollistaa kodissani verkkoyhteydet sekä WiFI, että ethernet kytkennät. Infraan kuuluu myös henkilökohtainen pöytätietokoneeni ja kannettava tietokone. Lisäksi minulla pyörii 24/7 Raspberry Pi 4:lla pieni muotoinen "palvelin", jossa pyörii erilaisia palveluja. Esimerkiksi Raspberry Pi:n päällä pyörii jatkuvasti PiHole ja Caddy webbi palvelin. IoT-laitteita minulla on taloudessani kaksi. Toinen niistä on TP-link Tapo C100 valvontakamera ja toinen on RGB-lamppu. Valvontakameran tarkoitus on mahdollistaa minulle kodin valvonta, silloin kun en ole itse paikalla. Tätä varten minun tulee vielä luoda WireGuard palvelulla VPN-tunneli, jotta pääsen turvallisesti siihen ulkoverkosta ja niin, että se ei käytä valmistajan palvelimia siihen. Puolestaan lamppu vain mahdollistaa kivan visuaalisen ilmeen kotiini.
* Kurssilla käytettävään laitteistoon minun puolelta kuuluu pääosin kannettavatietokoneeni ja mahdollisesti joissain tapauksissa pöytäkoneeni kotona. Kannettavalla minulla on käytössä Oraclen VirtualBox ohjelmisto, joka mahdollistaa virtuaalikoneen käytön kurssin tehtävissä. Kurssilla käytän Debian pohjaista Kali Linux virtuaalikonetta. Myös puhelimeni muodostaa osan tästä kokonaisuudesta, koska sen avulla voin suorittaa kaksivaiheisen autentikoinnin kirjautuessani koulun järjestelmiin. Tämän tarkoitus on lisätä tietoturvan tasoa merkittävästi.
* Tieto ja data muodostuu kurssinmateriaaleista, itseni ja muiden opiskelijoiden GitHub-repositoreista. Tämän lisäksi saatamme päästä hyödyntämään erilaisia "laboratorioita", joissa simuloimme erilaisia hyökkäysmenetelmiä.


a2) What is excluded from the scope and why

* Tästä arvioimastani "scopesta" ulos jää taloyhtiöni naapureiden omat lähiverkot, tietokoneet ja älylaitteet. Lisäksi kaikki työnantajani laitteet ja sovellukset eivät kuulu tähän. Oma Nintendo Switch konsolini myöskään ei kuulu tähän listaan.
* Nämä kaikki jäävät scopesta ulkopuolelle useista syistä. Naapuruston verkkolaitteet eivät ole mitenkään minun hallinnassa, koska en omista niitä. Puolestaan työnantajani laitteet ja sovellukset kuuluvat työnantajan ympäristöön, eikä omaani. Vaikka pelikonsoli on kytketty verkkoon, se ei kuulu tähän kokonaisuuteen laitteista.


a3) Key interfaces and boundaries

* Tässä yhtedessä keskeisimpinä pilviteknologiasta, joita hyödynnetään on GitHub.
* Keskeisimmät etäyhteysmenetelmät ovat SSH-yhteys esimerkiksi pöytäkoneeltani Raspberry Pi palvelimelle tai virtuaalikoneellani yhteyden muodostaminen toiseen koneeseen. Lisäksi käytän WireGuardin VPN-yhteyttä päästäkseni ulkoverkosta sisäverkkooni turvallisesti ja näin pääsen kamerakuvaan. Itse kamerakuvan muodostamiseen hyödynnän RTSP-protokollaa.
* Internetpalveluntarjoajan reitittimen sisäinen palomuuri ja Raspberry Pi:llä pyörivä PiHole muodostavat rajat liikenteelle internetin ja kotiverkkoni välillä.



Mallinnus scopesta

<img width="1176" height="1075" alt="h1-liite" src="https://github.com/user-attachments/assets/47d35f70-4b7a-485a-99f5-895e59aea906" />





What evidence could I present?

Listaa esimerkkitodisteista 


* Lista virtuaalikoneista (Sisältää omia projekteja ja kursseilla käytettyjä koneita).
  <img width="1182" height="588" alt="image" src="https://github.com/user-attachments/assets/cd4849b7-ae55-4446-98f5-52fea95b0886" />

* Kuvankaappaus reitittimen hallintapaneelista. Siellä näkyy myös laitteistoa, jota kytketty lähiverkkoon.
  <img width="988" height="714" alt="image" src="https://github.com/user-attachments/assets/7139acdc-444e-426f-8e47-4002ae217560" />

* Kuvankaappaus pöytäkoneeni järjestelmätiedoista ja komponentti listasta.
  <img width="1287" height="806" alt="image" src="https://github.com/user-attachments/assets/7d7f5bf8-098e-45a5-b4c5-ffdd4c8db7ca" />

* Kuvan kaappaus terminaalistani, jossa olen ottanut SSH-yhteyden Raspberry Pi palvelimelleni.
  <img width="1210" height="416" alt="image" src="https://github.com/user-attachments/assets/2e06a7c5-32d3-4d74-b7c3-e6e64f0014b8" />


B) Linking the Assignment to the Standard

Alla havainnollistava kuva, jossa on eritelty kohteet, niiden tarpeet, ISO 27001 viittaus ja todiste jokaisesta.
<img width="1398" height="728" alt="image" src="https://github.com/user-attachments/assets/4e7190c2-25f3-417a-8921-6b1e5cf27c2f" />



Lähteet:
* Karvinen, T. 2026. Sovellusten hakkerointi. Luettavissa: https://terokarvinen.com/application-hacking/. Luettu: 24.8.2026

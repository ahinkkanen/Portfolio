# H4 NFC ja RFID

## a) Tarkastele käytössäsi olevia RFID tuotteita, mieti miten hyvin olet suojautunut RFID urkinnalta?

Minulla oli käytössä vain rajallinen määrä tuotteita kotoani, jossa on käytössä RFID. Aloitin keräämällä erilaisia kortteja, kuten pankki- K-plussa ja kirjastokorttini. Tähän lisäksi otin tarkkailuun työpaikkani kaksi erilaista "tagia", joita lähdin tarkastelemaan. Tutkimusta varten latasin puhelimeeni ````Ìphone 15 Pro```` ````App Store````:sta sovelluksen ````NFC Tools````, jolla oli tarkoitus analysoida tuloksia. Harmikseni yrittäessäni saada tuloksia työpaikkani kulku tageistä en saanut mitään irti, enkä myöskään omasta pankki- tai K-plussa kortista. Ainoa, josta sain tuloksia oli ````Helmet````:n kirjastokorttini. Kiinnitin huomiota, että kyseisen kortin takakannessa myös luki ````RFID````, jolloin voin varmaksi todeta kirjastokorttini käyttävän ````RFID```` -teknologiaa.

Selvitin mahdollisia syitä, miksi muut eivät toimineet samalla tavalla. Selvisi, että muiden korttien ja tagien käyttämä NFC/RFID-tekniikka ja tietojen suojaus menetelmät todennäköisesti eroavat toisistaan ja täten ````Iphone 15 Pro:n```` käyttämä ````NFC Tools```` ei onnistunut saamaan niistä tietoja ulos. Olisi ollut mielenkiintoista saada tähän enemmän tutkittavaa materiaalia, mutta sitä ei ollut valitettavasti nyt saatavilla.

#### Alla olevassa kuvassa näkyy tuloste, joka tuli skannatessani kirjastokorttini. Tästä kuvasta kaikki data on peitetty.

<img width="1179" height="2556" alt="image" src="https://github.com/user-attachments/assets/a1ec6402-b796-4e5f-b126-6f6a4a2b7540" />

### Pohdintaa omasta suojautumisesta RFID urkintaa vastaan

Tässä harjoituksessa todentui, että ainakin korttini tuntuvat olevan suhteellisen hyvin suojattuja RFID-urkinnalta, koska kirjastokortti oli ainoa, josta sain luettua tiedot. Myöskään kirjastokortti tuskin pitää suhteellisen arkaluonteisia tietoja sisällään, joten tämä ei haitannut minua lainkaan. Huolestuneempi olisin ollut, mikäli Iphonella olisi voinut saada luettua esim. pankkikortin tietoja. Toki tässä tulee myös ymmärtää, että Iphone ei ole välttämäti parhain lukemaan näitä ja sekin saattaa omistaa sisällään tiettyjä rajauksia, jotka estävät sitä tiedon lukemiselta. Myös suojaus työleimaimien kohdalla näillä testeillä tuntuu olevan kohdillaan. Näissäkin voi olla tokin eroja, mikäli käyttää eri laitteita urkintaan. Ainoana asia, jonka löysin suojaaman itseäni urkinnalta oli minun lompakko, joka on ````RFID```` suojattu. Muita ulkoisia asioita en löytänyt, jos tarkoitus oli saada muita, kuin salattuja kortteja ja tageja.




## b) Tutustu APDU komentojen rakenteeseen.

#### Claude Sonnet 5.5 Low määritelmä APDU komentojen rakenteesta


APDU (Application Protocol Data Unit) on ISO/IEC 7816-4 -standardin määrittelemä viestiyksikkö, jolla lukija ja älykortti keskustelevat keskenään. Lukija lähettää kortille komento-APDU:n, ja kortti vastaa vastaus-APDU:lla. Myös NFC-kortit käyttävät samoja viestejä langattomasti.

Komento-APDU koostuu otsikosta (CLA, INS, P1, P2) ja valinnaisesta rungosta (Lc, Data, Le). CLA kertoo käskyn luokan, INS itse käskyn, P1 ja P2 käskyn parametrit, Lc lähetettävän datan pituuden, Data itse datan ja Le vastaukselta odotetun pituuden. Vastaus-APDU sisältää mahdollisen datan sekä statustavut SW1 ja SW2, joista 90 00 tarkoittaa onnistumista.

Tietoturvan kannalta APDU:t ovat tärkeitä, koska relay-hyökkäyksessä hyökkääjä välittää juuri nämä viestit kortin ja lukijan välillä. Esimerkiksi tänä vuonna löydetty WindRelay-haittaohjelma välitti pankkikortin APDU-viestejä reaaliajassa rikollisten laitteelle. Salausta ei siis tarvitse murtaa, riittää että viestit liikkuvat kortin ja lukijan välillä.

#### Oma pohdinta APDU komentojen rakenteesta
APDU on älykorttien ja lukijalaitteiden välisessä tiedonsiirrossa käytettävä viestimuoto, jonka avulla laitteet voivat lähettää komentoja ja vastaanottaa vastauksia. APDU-viesti koostuu komentoluokasta, käskystä ja sen parametreista sekä mahdollisesta datasta. Vastauksessa kortti palauttaa pyydetyt tiedot sekä tilakoodit, jotka kertovat, että onnistuiko komento. APDU-viestejä käytetään esimerkiksi pankkikorteissa, SIM-korteissa ja NFC-tunnistautumisessa. Ne ovat myös tietoturvan kannalta merkittäviä, sillä viestien välittäminen kortin ja lukijan välillä voi mahdollistaa erilaisia relay-hyökkäyksiä.

## c) Tutki ja kerro minkä mielenkiintoisen RFID hakkerointi uutiset löysit.

### Hackers build a 'Master Key' that unlocks millions of Hotel rooms

https://thehackernews.com/2018/04/hacking-hotel-master-key.html

Uutinen on sivustolta ````The Hackers News```` poimittu artikkeli, joka koskee tutkimusta, jossa suomalaiset hakkerit/tietoturvatutkijat ovat kyenneet rakentamaan ````Master Key````:n, jonka avulla pystytäään murtautumaan miljooniin hotellihuoneisiin. Vaikka uutinen on jo vanha (````26.04.2018````) oli se silti todella mielenkiintoinen luettava. Tosiaan tuolloin suositussa elektronisessa lukitusjärjestelmässä havaittiin suunnitteluvirhe, joka mahdollisti kaikkien lukittujen huoneiden avaamisen. Kyse oli Assa Abloyn Vision by VingCard -lukitusjärjestelmästä, joka on käytössä yli 42 000 kohteessa 166 maassa. Kehittäjinä tälle ````Master Key````:lle olivat F-Securen tutkijat Tomi Tuominen ja Timo Hirvonen, jotka rakensivat tuhansien työtuntien jälkeen tämän avaimen, joka avasi minkä tahansa järjestelmää käyttävän hotellihuoneen. Teoriatasolla hyökkäys vaati vain yhden kohteen avainkortin. Sen tiedot saattoi lukea etäältä vieraan taskusta tai hankkia varaamalla huoneen. Sitten muutaman sadan euron RFID-lukija/kirjoittaja ja tutkijoiden oma ohjelmisto riittivät luomaan yleisavaimen minuuteissa. Laite kokeili lukon luona eri avaimia alle minuutin ja sieltä pystyi murtamaan avaimen ja avata oven jättämättä jälkeä järjestelmään. Hyökkäystä ei tiettävästi käytetty todellisessa maailmassa. Valitsin tämän uutisen, koska luennolla Lari mainitsi käsitteen ````Master Key```` ja se vaikutti mielenkiintoiselta ja haastavalta toteuttaa.


## Lähteet:

* Claude Sonnet 5.5 Low
* https://terokarvinen.com/verkkoon-tunkeutuminen-ja-tiedustelu/
* https://smartcardfyi.com/guide/apdu-command-reference/
* https://thehackernews.com/
* https://thehackernews.com/2018/04/hacking-hotel-master-key.html

# H1 Korva netissä

## a) WebSDR

Valitsin ````WebSDR.org```` sivustolta Brazilialaisen ````Pardinho```` radiokanavan, jota lähdin tutkimaan, koska se vaikutti mielenkiintoiselta. Harjoituksen aikana radiolla oli 107 aktiivista kuuntelijaa. Katsoin alla olevaa jatkuvasti päivittyvää signaalinvahvuuden osoitinta. Sieltä vieritin osoittimen kohtaan, josta signaali näytti huomattavasti vahvimmilta. Tämä oli taajudeltaan 6990.0 kHz. Täältä kuului selkeää puhetta, vaikka kieli oli täysin vieras. Kuitenkin huomaa, että kyseessä on todella kaukainen paikka ja valitsemalla lähempänä toimivan radion, niin ääni olisi vielä laadukkaampi.

Alla olevassa kuvassa näkyy WebSDR:n kautta oleva radioyhteydenotto Pardinhoon. Kuvassa ilmenee asetukseni, joita käytin.

<img width="2018" height="1208" alt="image" src="https://github.com/user-attachments/assets/32ecc59f-133d-40ee-9cc0-298b291fe418" />

Aallon pituuden laskemiseen käytin ````https://www.wavelengthcalculator.org/```` palvelua. Tähän syötin taajuuden ja ohjelma laski arvioidun aallonpituuden. Arvioitu aallonpituus on 42,89 m. 

<img width="1436" height="1338" alt="image" src="https://github.com/user-attachments/assets/de7e05b4-7043-45f8-88f3-eb5d4ab452a7" />

#### Tiedot

````
- Taajuus: 6990 kHz
- Aallonpituus: 42,89 m
- Modulaatio: LSB
````

## B) Moduwhat?

Tätä harjoitusta varten valitsin WebSDR palvelusta ````Maasbree Netherlands```` radiokanavan. Kuuntelin tätä osoittimen mukaisesti parhaalta taajuudelta, joka oli ````3601.35````. Nyt vaihdoin modulaatioita. Aikaisemmassa käytin ````LSB````, mutta nyt otin käyttöön ````AM````. Täältä kuulin täysin selvää puhetta. Tämä todennäköisesti tapahtui, koska kanava on fyysisesti itseäne huomattavasti lähempänä. Kuitenkaan en saanut tässä irti, miten modulaation vaihto vaikutti, koska en huomannut eroa. 


Alla kuva näkymästä.

<img width="2250" height="1524" alt="image" src="https://github.com/user-attachments/assets/43c37c4d-689e-4410-8f3b-dd7980cee00d" />

#### Tiedot

````
- Taajuus: 3601.35 kHz
- Aallonpituus: 83.241 m
- Modulaatio: AM
````


## C) ADS-B

Aloitin tehtävän tutkimalla sivuston kautta lentokoneita. Löysin Saudi Arabian kohdalta ulkoisesti suuri kokoisen koneen, joka paljastuikin olevan sotilaslentokone. Kyseinen kone on lähtenyt Dohasta liikkeelle, mutta määränpäätä ei selvinnyt. Myöskin moni koneen tieto oli vain määritetty (n/a), koska kyseessä on sotilaskone, joten sen kaikkea dataa ei tahdota jakaa yleisesti julkisuuteen. 

#### Tässä kuvassa näkyy lentokone kartalla.

<img width="2174" height="1618" alt="image" src="https://github.com/user-attachments/assets/7abeb1b6-0a2f-42da-8947-443fdde79964" />

#### Tässä kuvassa ilmenee lentokoneen ja lennon yksityiskohtaisia tietoja.

<img width="132" height="1232" alt="image" src="https://github.com/user-attachments/assets/0ec16f1e-6264-45f6-a021-1d520bc0d8dd" />

#### Tiedot

````
- Kutsutunnus: LHOB287
- Hex: 06A27A
- Rekisteri: A7-MAM (Qatar)
- Lentoyhtiö: n/a
- Tyyppi: C-17
- Barometrinen korkeus: 34 000 ft
- Lokaatio (kuvan hetkellä): 28,991°, 42,538°
````

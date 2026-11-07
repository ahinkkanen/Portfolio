<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/13e807ae-8cfd-4f38-bf6d-d67e4187ba23" /><img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/e0b1bf85-c30a-43bb-99ec-0ab84ec11fab" /># H3 Aaltoja harjaamassa


## x) Lue ja tiivistä.

#### Hubacek 2019.

- Videossa mallinnetaan, kuinka URH:n avulla pystytään nauhoittamaan kulkevaa signaalia
- Videossa demonstroidaan, miten siepattua signaalia voidaan analysoida tarkemmin
- Videossa pureudutaan signaalin demodulaatioihin ja myös bitti tason työskentelyyn


#### Cornelius 2022. 

- Sääaseman ottamaa dataa lähdettiin purkamaan rtl-433:sta hyödyntäen ohjelmaa
- Signaaleja analysoitiin hyödyntäen URH
- Saatuja signaaleja myös URH:n avulla demoduloitiin


## b) rtl_433.

Etsin selamen kautta ````rtl_433```` GitHub repositorion. Tämä löytyy ohjeman tekijän ````merbanan```` repositoriosta.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/a171c9cb-6ab3-49bb-a1f7-32d221facd29" />

GitHub repositoriossa on selkeät ohjeet asennukseen eri alustoille ja myös ajo ohjeet. 

Softa radion asennus Linuxilla ````sudo apt update```` päivittää pakettilistat ja komennolla ````sudo apt install rtl-433```` asennetaan itse softa radio ohjelma koneelle. Ohjelma ajetaan käyntiin terminaalista syötteellä ````rtl_433````. 

#### Itse olin jo asentanut rtl_433 aikaisemmin.
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/84f10b80-4bd8-4cbf-b3a1-2cd3bdecafc8" />

#### Ohjelman ajo

Kun ajaa terminaalissa ````rtl_433 -h```` ohjelma lähtee käyntiin ja näyttää sen version alussa ja parametreistä ohjelistan. 

Käyttämäni ohjelma version on ````rtl_433 version 25.02 (2025-02-19)````.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5b22e62d-b4ad-4a5f-aefc-c8a1abcce6aa" />


## c) Automaattinen analyysi.


Harjoitusta varten latasin tiedoston ````terokarvinen.com```` sivustolta. Tiedostolle määritettiin aluksi viel ajamista varten oikeudet.


<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/e13986fe-3bed-471a-8ef0-50f1c86e87b5" />


Katsoin ````rtl_433```` -ohjelimstoon ````help```` -sivuilta ohjeita mahdollisista parametreista. Tässä myös kysyin ````CLaude Sonnet 5.5 Low```` -kielimallia vielä ehdottamaan näistä hyödyllisintä ja sieltä nousi parametri ````-r````. Tämä mahdollistaa datan suoran lukemisen suoraan tiedostosta.


<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/862a3c71-b256-46cb-8799-8ea622f03671" />


Näkymä kun ohjema on ajettu harjoitustiedostolle ````Converted_433.92M_2000k.cs8````.


<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5724a615-27f3-4def-8794-945285b8c68e" />


#### Analyysi näytteestä

Näytteessä ilmenee mahdollisesti kolmen eri laitteen siepattuja signaaleja. Tässä hypoteesissa ne olisivat ````KlikAanKlikUit-Switch````, ````Proove-Security```` ja ````Nexa-Security````. Huomasin, kuitenkin pian toistuvan logiikan näytteestä, jossa samat mallit tulevat kolmessa osassa nejä kertaa samassa järjestyksessä. Aloin pohtimaan voiko tämä silti, jotenkin tulla yhdestä laitteesta, koska jokaisessa näytteessä ````id / House Code```` on jokaisessa tulosteessa sama ````8785315````. Tutkin netistä ovatko nuo kolme eri valmistajaa vai, mikä niiden tarkoitus on niin minulle selvisi, että ne ovat eri merkkejä, mutta tekevät saman asian vain varmistaakseen, että signaalin viesti menisi varmasti perille. Numero koodi on vain lähettäjä laitteen yksilöity nimi.


## d) Too compex 16?

Tehtävää varten ladattiin ````terokarvinen.com```` -sivulta harjoitustiedosto, joka on nauhoitettu ````urh```` -ohjelmalla. Koska näyte on otettu ````urh```` -ohjelmalla, on sen tiedostopääte ````.complex16s````. Jos tätä lähtisi itsessään analysoimaan suoraan hyödyntäen rtl_433 ohjelmistoa, niin se ei onnistuisi, koska ````rtl_433```` ei tunnistaisi tuota ````.complex16s```` -tiedostopäätettä. 

Alla olevassa kuvassa ilmenee ongelmani, kun pyrin ajamaan tiedostoa ````rtl_433```` ohjelmalla.

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/0b79fb41-776b-4dd0-a314-ea3d495ec01d" />


Jotta pystyn analysoimaan tiedostoa käyttäen ````rtö_433```` -ohjelmaa, niin tein kopiontiedostosta, jonka tiedosto pääte oli eri (````.cs````). 

````
cp Recorded-HackRF-20250411_183354-433_92MHz-2MSps-2MHz.complex16s d-kaannetty.cs8
````

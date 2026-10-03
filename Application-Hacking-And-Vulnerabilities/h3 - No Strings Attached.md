# h3 No Strings Attached

## a) Strings.

Latasin Virtuaali Kaliin harjoitus tiedoston
````
ezbin-challenges.zip
````

Tämä harjoitustiedosto latautui "Downloads" kansioon josta purin sen komennolla "unzip".

````
unzip ezbin-challenges.zip
````
<img width="845" height="349" alt="image" src="https://github.com/user-attachments/assets/9ee95d99-8999-472e-a7b1-76543e7515b1" />
<img width="1065" height="617" alt="image" src="https://github.com/user-attachments/assets/e4d9dcb6-2b16-4ff1-93ba-4aa5328ab20d" />
<img width="1318" height="729" alt="image" src="https://github.com/user-attachments/assets/93731f92-f302-4d46-a216-e31361e16beb" />

Seuraavaksi ajoin ohjelman.
````
./passtr
````
Se kuitenkin pyysi salasanaa jota en tiennyt.
<img width="1242" height="293" alt="image" src="https://github.com/user-attachments/assets/62486f68-49c9-42cc-b80a-6617a0253bd7" />

Ajoin seuraavaksi ajoin "strings" komennon "passtr" nimisen hakemiston sisällä. Tämä purki sen osiin ja sieltä paljastui etsimäni salasana ja flagi.

<img width="1827" height="1337" alt="image" src="https://github.com/user-attachments/assets/441a7029-05d4-471a-b4ad-eeb944ff17a9" />

````
salasana: sala-hakkeri-321
````

````
flag: FLAG{Tero-d75ee66af0a68663f15539ec0f46e3b1}
````


## b) Make a new version of the passtr.c program where the password doesn't appear directly as-is in the binary.

Tehtävässä jouduin käyttämään apuna koodin muokkaamisessa Copilot tekoälyä (Copilot Smart). Minulle C-ohjelmointikieli on täysin vieras, enkä ole koodannut sillä mitään. Alkuperäinen koodi sisälsi salasanan suoraan merkkijonona ja siksi strings työkalulla sen avasi sen suoraan. Muokkaamani koodi purki salasanan pienempiin osiin, niin ettei se ole yhtenä merkkijonona koodissa. Tämän takia salasana ei paljastu suoraan binäärissä, kun sitä tarkastelee.

Navigoin itseni passtr.c tiedostoon ja avasin sen käyttäen micro tekstieditoria.
<img width="1486" height="787" alt="image" src="https://github.com/user-attachments/assets/b6e814f1-de1f-496b-9f8a-b7e6164d325f" />

Alkuperäinen passtr.c koodi.
<img width="2116" height="1224" alt="image" src="https://github.com/user-attachments/assets/1e7fd18a-66d2-4448-9b42-b9123ce8b54e" />

Muokattu passtr.c koodi. Tässä...
<img width="2108" height="1390" alt="image" src="https://github.com/user-attachments/assets/794f1f42-a5bb-4202-9db9-7775966362e8" />

Kokeilin purkaa ohjelman binääriksi strings passtr komennolla, mutta nyt sieltä ei samalla tavalla paljastunut salasana. 
<img width="2172" height="1300" alt="image" src="https://github.com/user-attachments/assets/f341593f-50f9-4763-8db2-8ce35ebf0e32" />

Testasin alkuperäisen salasanan toimivuutta ohjelman suorittamiseen ja se onnistui.
<img width="1842" height="282" alt="image" src="https://github.com/user-attachments/assets/fb15dc72-dcde-483c-a52b-a92460831ef9" />

Yhteenvetona uusi koodi tosiaan purki salasanan, niin että se ei ilmene binäärinä yhdessä merkkijonossa vaan se on pilkottu. Kuitenkin kun yrittää avata ohjelman ja syöttää alkuperäisen oikean salasanan, niin ohjelma toimii oikein.


## c) Packd. 

Lähestyin c) tehtävää myös samalla tavalla kuin a) tehtävää. Navigoin itseni oikeaan osoitteeseen ja yritin ajaa ohjelman. Ohjelma kysyi salasanaa, jota en tiedä ja kokeilin jälleen samaa "admin" salasanaa. 
<img width="1842" height="714" alt="image" src="https://github.com/user-attachments/assets/9523f98a-22a0-47f5-9170-66da4c234360" />

Jatkoin samaa lähestymistä suorittamalla strings komennon packd tiedostolle. Luulin jo hetken, että onko tämä yhtä selkeä kuin eka tehtävä, mutta ei ollut.
````
strings packd
````
<img width="1816" height="1406" alt="image" src="https://github.com/user-attachments/assets/b9dff8e0-b10e-467d-aa46-9ac4981d3c72" />

Kokeilin olettamaani "piilos-An" salasanan toimivuutta ohjelman suorittamiseen, mutta se ei toiminutkaan.
<img width="1300" height="298" alt="image" src="https://github.com/user-attachments/assets/cdb03053-43c0-4cfc-8014-99e3cf4b54bb" />

Olin umpikujassa ja tarvitsin apua vihjeistä. Sovelsin vihjeiden komentoja ja ajoin ne terminaalissa. Sieltä selvisi, että paketti on pakattu UPX ohjelmalla. Mietin voisinko unzip tyylisesti purkaa tiedoston. 
<img width="1974" height="1168" alt="image" src="https://github.com/user-attachments/assets/5ca7d559-4ade-42b6-8c22-701b7957d5c2" />

Netistä löysin ohjeet kuinka purkaa UPX pakattu ohjelma. Tässä käytettetiin yhteydessä -d parametria, joka purkaa pakkauksen.
<img width="2014" height="1046" alt="packd" src="https://github.com/user-attachments/assets/b0c7dfc0-3107-46fa-87c2-0beb0b1a98e1" />

Sitten purin pakkauksen.
````
upx -d packd
````
<img width="2044" height="622" alt="image" src="https://github.com/user-attachments/assets/0137f0b6-07b7-4dc6-a22c-237df08f6e2f" />

Sitten testasin uudelleen strings työkalulla tarkastella nyt oletettavasti puretin paketin binäärin tarkastelua. 
````
strings packd
````

Sieltä paljastui uudenlainen salasana ja myös flagi näytti olevan nyt kokonainen verrattuna aikaisempaan. 
<img width="1782" height="1118" alt="image" src="https://github.com/user-attachments/assets/4185da3c-4db5-48a9-8eb3-1a71a2416574" />

Testasin vielä toiseen suuntaan ajaa ohjelman ja syöttää uuden löytämäni salasanan. Tämä onnistui ja flagi tulostui.
<img width="1900" height="300" alt="image" src="https://github.com/user-attachments/assets/1dd96ef8-a2ba-4c5a-8746-732f54e1e9c5" />


Lähteet:
- Karvinen, T. 2026. Sovellusten hakkerointi. Luettavissa: https://terokarvinen.com/application-hacking/. Luettu: 8.9.2026.
- yoshI. Manually Unpacking UPX | PE & PE+ (x86/x64 Tips). Luettavissa: https://yoshlsec.github.io/manuallyupx/. Luettu: 8.9.2026.

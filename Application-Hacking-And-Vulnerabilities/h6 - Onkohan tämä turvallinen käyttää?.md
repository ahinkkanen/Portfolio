# h6 Onkohan tämä turvallinen käyttää?

Aloitin tehtävän ratkomisen ````make```` komennolla, jolla käänsin lähdekoodin suoritettavaksi ohjelmaksi. Se ei onnistunut. koska tarvittavaa kirjastoa ei ollut valmiina. Asensin sen ````sudo apt install libssl-dev````. Tämä korjasi tilanteeni.

<img width="2100" height="612" alt="image" src="https://github.com/user-attachments/assets/a60ef188-6881-441d-ad39-3ae90efc15e0" />

Tässä kohtaa olin saanut ohjeman ajettavaksi ja pääsin suorittamaan sen ohjelmakoodille ````Tapo_C200v4_en_1.4.2.bin````. Koko komento oli ````./tp-link-decrypt Tapo_C200v4_en_1.4.2.bin````. Sieltä sain avaimen paljastettua, mutta sillä en tehnyt mitään.

````
key/iv:
KEY=9c6ba1d761e4eee17dfde90cfed603bd
IV=8778f31423815ce85e9f186b60507edd
````


<img width="2128" height="1312" alt="image" src="https://github.com/user-attachments/assets/b550e400-23b0-4262-a184-0e055794426a" />

Seuraavaksi latasin moodlesta ````dump-tapo-c200v3-1.4.2.bin````, jota varten ohjeista kopion ohjeman, joka oli tarkoitus ajaa tälle. Vielä ennen ajoa loin ````output```` nimisen hakemiston kansion sisään, johon oli tarkoitus tulla kirjoittamani script.py skriptin tulostus. Sieltä paljastui mielenkiintoisia uusia tiedostoja, jotka vaikuttivat aluksi todella lupaavilta, kuitenkaan lopulta en saanut näistä irti mitään merkittävää. Koitin tutkia Ghidralla ja muilla työkaluilla tiedostoja, mutta en saanut seuraavaa, johtolankaa. Olin täydellisessä umpukujassa. Tarkoitus oli tutkia rootfs.bin, rootfs_data.bin ja kernel.bin tiedostoja, mutta en saanut niistä mitään irti.

<img width="1672" height="430" alt="image" src="https://github.com/user-attachments/assets/98ed4ebd-44d8-4c49-ace0-44cb83b3cebb" />

````output```` hakemiston sisältö. 

<img width="1956" height="828" alt="image" src="https://github.com/user-attachments/assets/97dc70f3-2313-4dcd-a908-c43570eadd33" />

Vein ````kernel.bin```` Tiedoston Ghidraan, mutta se ei auttanut minua eteenpäin. Kokeilin myös ajaa ````binwalk3```` työkalua rootfs.bin tiedostolle ja sieltä selviää, että se sisältää dataa, mutta ei sellaista, josta olisi tässä suoraan konkreettista hyötyä.

<img width="822" height="910" alt="image" src="https://github.com/user-attachments/assets/2881c7fd-0c99-4b91-97f6-ef9b9a58126c" />

Tässä vielä tutkin ````kernel.bin.extracted```` tiedostoa, mutta sieltä ei paljastunut myöskään, mitään mikä olisi vienyt minua eteenpäin tehtävässä.

<img width="1862" height="822" alt="image" src="https://github.com/user-attachments/assets/217c5436-7c56-4207-85a2-c4e625192131" />

Olin totaalisessa umpikujassa ja otin askelia taaksepäin ja päätin lähteä kokeilemaan kaikkia hakemistoja ja tiedostoja alusta ja suoritin niille binwalk komentoja. Käytin tässä apuna Claude Sonnet 5 kielimallia, jotta voisin saada uusia näkökulmia tehtävän ratkaisua varten.

<img width="1936" height="754" alt="image" src="https://github.com/user-attachments/assets/41514105-3848-4435-8e36-9c96a7f627b8" />

Testasin vielä muutamaa Clauden suosittelemaa testiä ja ne tuottivat tulosta.

<img width="2100" height="982" alt="image" src="https://github.com/user-attachments/assets/9244130c-3f6f-411d-aab7-cc21128a9452" />

Tässä näkyy kun löytyy /etc hakemisto. Seuraavaksi tarkoitus oli lähteä tutkimaan sitä. Kuitenkaan ei paljastunut mitään salasanoja, joita olisin voinut päästä tarkastelemaan.

<img width="1610" height="558" alt="image" src="https://github.com/user-attachments/assets/4c60c36d-ef55-4fb2-96bf-fc168567130b" />

<img width="2164" height="1008" alt="image" src="https://github.com/user-attachments/assets/9e08cd26-b8b6-4b8b-9e8c-7c1b1b2c5fac" />

Ajoin Clauden skriptin, jonka tarkoitus oli vielä löytää piilotettuja squashfs tiedostoja ja löysinsieltä mahdollisen uuden ````_rootsfs_data.bin.extracted````, jossa sisällä hakemisto ````squashfs-root````. 

<img width="1784" height="1284" alt="image" src="https://github.com/user-attachments/assets/cbbe16b1-355d-4971-a581-5d9e238e0b64" />

Tässä olen siirtynyt ````squashfs-root```` hakemistoon, mutta sen sisältö osoittautui kuitenkin samaksi.

<img width="982" height="536" alt="image" src="https://github.com/user-attachments/assets/2db3c0ad-ffb8-40fd-8998-9272aebb7f71" />

Tässä kohtaa taitoni loppuivat, enkä keksinyt miten edetä. Tehtävä opetti minulle kuitenkin ajattelu tapaa miten tällaista haastetta lähestytään ja mitä menetelmiä käytetään. Tehtävä oli todella haastava, mutta mielenkiintoinen ja realistinen harjoite. Tiedostan, että harjoitus olisi mahdollista ratkaista, mutta omat taidot eivät siihen vielä riittäneet. Haavoittuvuutta voidaan varmasti hyödyntää pahantahtoisesti. Onnistuin kuitenkin purkamaan ohjelmaa ja analsoimaan sitä. Pääsin kohtuullisen pitkälle tehtävässä mielestäni, vaikka lopullinen ratkaisu jäi saavuttamatta.

## Lähteet:

- Claude by Antrhopic, Sonnet 5 (High).
- Karvinen, T. & Iso-Anttila, L. 2026. Hardware hacking. Sovellusten hakkerointi ja haavoittuvuudet. Opintojaksomateriaali Moodlessa. Haaga-Helia ammattikorkeakoulu. Luettu 29.9.2026.
- Karvinen, T. 2026. Sovellusten hakkerointi. Luettavissa: https://terokarvinen.com/application-hacking/. Luettu: 29.9.2026.




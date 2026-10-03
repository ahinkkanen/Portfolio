# h2 Break & Unbreak

## x)
- OWASP TOP 10: A01 Broken Access Control. Tämä on ollut vuoden 2021 OWASP:n tuottaman listan kärjessä. Siinä viitataan yksinkertaisesti tilannetta, jossa toisella käyttäjällä on kyky päästä tekemään asioita, joihin todellisuudessa hänellä ei pitäisi olla oikeuksia.
- Fuff on suomalaisen Joona Hoikkalan rakentama weppi fuzzeri, jonka tarkoitus on mahdollistaa piilotettujen hakemistojen etsimisen. Fuff:lla on myös kyky fuzzata myös headereita ja POST-parametrejä. Tämä työkalu on oleellinen osa hakkerointia ja sen avulla weppi palvelimen todellisia sisältöjä on helppo kartoittaa.
- Access control vulnerabilitites and privilege escalation: Access controllin tarkoitus on määrittää ja todentaa kelläkin käyttäjällä on pääsy toimintoihin. Pohdin onko Zero Trust periaate hyvä ja käytännöllinen tässä tapauksessa? Käyttäjien identifionti ja tarkat määritykset oikeuksille parantavat tilannetta.
- Raporttien tulisi noudattaa akateemista tyyliä lähteiden käytön kanssa. Lisäksi raportin tulee olla lukijalle helppolukuinen ja täsmällinen, niin että vaikeat asiat ovat selitetty selkeästi ja miksi niin on tehty. Kaikkien teknisten komentojen tulisi olla kirjattuja ja mitä niiden lopputulemana on syntynyt.

## Ympäristöni
- Operating System: Debian (64-bit)
- Browser: Firefox 140.11.0esr
- Hardware: Processor: AMD Ryzen AI 9 365 w, RAM: 2GB, Disk: 80GB
- Network: Intel PRO/1000 MT Desktop (NAT)

## a) Break into 010-staff-only
Kun olin saanut harjoitus ympäristön ohjeiden mukaisesti pystyyn, aloin testaamaan syötteeseen erilaisia arvoja ja tekemään tulosteiden pohjalta olettamia. 

<img width="2880" height="1258" alt="image" src="https://github.com/user-attachments/assets/2d11d286-a874-48eb-8c72-e88178278148" />

Oletus arvolla "0" tulostui sivulla "not found". Tämä antoi alustavaa tietoa, että sivu jakaa selkeätä informaatioita siitä, mitä tietokannassa tapahtuu kun sinne lähettää kyselyn. Tämä liiallinen informaation jakaminen lisää myös hyökkääjän hyökkäyspinta-alaa merkittävästi. 

Seuraavassa kuvassa näkyy, kuinka tuloste on vaihtunut, kun olen antanut syötteeseen minun pin-koodin "123". Tällöin tuloste oli minun salasanaksi määritetty Somedude.

<img width="2880" height="1592" alt="image" src="https://github.com/user-attachments/assets/1c4de6db-0090-4bcd-9e5f-e6a0baf65867" />

Pian tämän jälkeen aloin syöttämään netistä yleisimpiä SQL-injektioita syötteeseen pin-koodin perään. Alla olevista kuvista näkee, kun pyrin ajamaan injektioita pin-koodin perään. Kuitenkin syöte jatkuvasti ilmoittaa, että syötteeseen voi antaa ainoastaan numeroja. 

<img width="2880" height="1514" alt="image" src="https://github.com/user-attachments/assets/0b890aad-4025-4622-935a-9144f03b3d02" />
<img width="2552" height="398" alt="image" src="https://github.com/user-attachments/assets/5f5e8718-38ff-4989-8cb6-83893847752d" />
<img width="2880" height="1452" alt="image" src="https://github.com/user-attachments/assets/29b5dd39-cb50-4345-a088-0655a9d3f1db" />

Pyrin pohtimaan, miten onnistuisin kiertämään tämän, jotta voisin ajaa syötteessä myös kirjaimia ja erikoismerkkejä, joka mahdollistaisi injektion toimivuuden. Pitkään mietin tätä sekä tutkin koodia ja löysin kohdan, jossa ohjelma vaatii numeroa. En kuitenkaan siinä kohtaan tajunnut, että pystyisin itse muokkaamaan koodia ja totaalisen umpikujan kohdalla tarvitsin apua vihjeistä. Sieltä vahvistui löytöni, joka liittyi juuri kyseiseen numero kohtaan. Kun poistin koodista alla näkävällä tavalla numero kohdan niin pääsin ajamaan syötteellä myös kirjaimia ja erikoismerkkejä. 

<img width="408" height="146" alt="image" src="https://github.com/user-attachments/assets/ac3460a6-65e9-4ab1-84de-a8f2c5463719" />


````
Alkuperäinen: <input type="number" name="pin" value="123">
````

````
Uudelleen muokattu: <input type="" name="pin" value="123">
````

Testasin saman tien uudestaan aiempia injektio versioita, joita olin kokeillut ennen tätä numero muutosta. Sain pitkästä aikaan hyvän olon tunteen kun tunsin oivaltaneeni idean ja miksi kokonaisuus toimi näin. Sain uudeksi tulosteeksi "foo". Tämä ei ollut kuitenkaan vielä lopullinen ratkaisu, mutta antoi lisää ideoita. Samalla myös huomasin kohdan joka helpotti tulevaa todella paljon. En ollut kiinnittänyt huomiota apuvälineeseen, joka oli sivun ala reunassa. Se mallinsi SQL-kieltä ja miten se funtkio hakee tietokannasta dataa. Aloin hyödyntämään tätä seuraavissa testeissä. 

<img width="2880" height="1546" alt="sql2" src="https://github.com/user-attachments/assets/5a3e0ec0-eccf-4dbf-82ba-64bcf797d756" />

Testasin eri injektio tyylejä, mutta ne johdattivat aina "Internal Server Error" näkymään. 
<img width="2876" height="1586" alt="image" src="https://github.com/user-attachments/assets/cf11e9e1-41d2-45ad-a60f-5bf2b521c0ae" />

<img width="2880" height="1582" alt="image" src="https://github.com/user-attachments/assets/72d41aa0-7913-4ac9-bd87-614453f4d0c5" />

Olin taas umpikujassa, eikä minulla ollut mitään ajatusta, miten pääsisin eteenpäin tai miten saisin injektioni läpi, koska SQL-kielenä ei ole minulle entuudestaan tuttu. Katsoin vihjettä ja sieltä selvisi UNION käyttö, jolla voidaan yhdistää kaksi pyyntöä samanaikaisesti. 

Alla oleva komento yhdistää alkuperäisen kysymyksen toiseen kyselyyn ja se palauttaa kaikki salasanat.
````
Komento: 123' UNION SELECT password FROM pins--
````

<img width="2874" height="1446" alt="image" src="https://github.com/user-attachments/assets/7217ba3f-9ba1-4221-958d-c3c3d0f62b09" />


Näin lopullinen haluttu admin password tuli esiin tietokannasta.

````
SUPERADMIN%%rootALL-FLAG{Tero-e45f8764675e4463db969473b6d0fcdd}
````


## b) Fix the 010-staff-only vulnerability from source code

Aloitin haavoittuvuuden paikkaamisen aluksi luomalla kopion tiedostosta, jota alan muokkaamaan, jotta vakavavan virheen sattuessa voin palauttaa alkuperäisen koodin tiedostoon. Tein sen alla alevalla komennolla.

````
cp staff-only.py copy-staff-only.py
````

Sitten avasin micro tekstieditorilla alkuperäisen staff-only.py tiedoston, jota tuli muokata.
<img width="1782" height="1328" alt="image" src="https://github.com/user-attachments/assets/5aa359e0-d0b8-4e9e-a938-55ec2b830c9a" />

Jouduin katsomaan ohjeista, miten koodi korjattiin, koska minun koodini vain rikkoivat sivun toimminnan. Alla olevassa kuvassa näkyy alkuperäinen koodi ja myös uusi korjattu koodi.
<img width="1982" height="1324" alt="image" src="https://github.com/user-attachments/assets/95dc7c13-e403-462d-9e0c-965d0e2b9714" />
<img width="2120" height="1386" alt="sql3" src="https://github.com/user-attachments/assets/14a2f15b-ee28-42e0-b53e-b8859e7c6ef9" />

Korjauksen jälkeen sivu ei palauttanut enää "SUPERADMIN flagiä". Eli korjaus oli suoritettu oikea oppisesti.
<img width="2880" height="1496" alt="image" src="https://github.com/user-attachments/assets/e19c4e4c-e816-4bf9-8ee7-daee03917d14" />

### Yhteenveto SQL-inketiosta
Harjoituksessa simuloitiin tietokannan syötteen manipuloimista. Haavoittuvuus liittyi syötteen liiallisen palutteen liialliseen informaatioon ja ohjelmistopuolen ratkaisuihin. Tehtävä oli itselle todella haastava, mutta opettavainen ja ymmärsin lopulta toiminnan periaatteet.






## c) Solve dirfuzt-1
Latasin ohjeiden mukaisesti tiedoston ja määritin sille samat oikeudet, mitä testitiedostolle teimme aiemmin.
<img width="798" height="498" alt="image" src="https://github.com/user-attachments/assets/7f5c85e1-6011-47c4-8473-f9636d7a42c1" />
<img width="2088" height="1332" alt="image" src="https://github.com/user-attachments/assets/4df92eeb-bf5a-450b-babd-39bcdbc0dd91" />

Sen jälkeen ajoin fuff työkalulla testi ympäristön ja se palautti minulle piilotettuja hakemistoja, joita voin syöttää oletus URL:n perään testasin niitä läpi ja kahdesta niistä löytyi flagit, joita etsin. Muut päätteet palauttivat saman flagin kuin pelkkä /.git/ pääte
<img width="830" height="340" alt="image" src="https://github.com/user-attachments/assets/e397e922-5b74-4464-a5a3-cd229d04e3f6" />
<img width="908" height="284" alt="image" src="https://github.com/user-attachments/assets/39169aec-47d7-4792-8063-309b239769dc" />

````
.git --> FLAG{tero-git-3cc87212bcd411686a3b9e547d47fc51}
````

````
wp-admin --FLAG{tero-wpadmin-3364c855a2ac87341fc7bcbda955b580}
````

## d) Break into 020-your-eyes-only
Ajoin fuff:n sivustolle, josta tuli yksi osuma. Se oli "admin-console". 
<img width="1932" height="1166" alt="image" src="https://github.com/user-attachments/assets/7033c283-71a8-48b1-9dd9-198cacb15f9e" />
<img width="1794" height="862" alt="image" src="https://github.com/user-attachments/assets/e2a418b9-8b28-40c7-9f60-36daebaa3cf0" />

Testasin laittaa piilossa olleen hakemiston URL:n perään, mutta se ei paljasanut uutta...
<img width="2880" height="1548" alt="image" src="https://github.com/user-attachments/assets/6de902f6-a187-4576-860b-efe8490bfada" />

Sen jälkeen loin itselleni tunnukset ja sitten liitin piilotetun hakemiston loppuun ja sieltä paljastui haluttu sivu.
<img width="2880" height="1588" alt="image" src="https://github.com/user-attachments/assets/cf64d3bd-4615-430d-b6cf-e627ca2b79a2" />



## e) Fix the 020-your-eyes-only vulnerability
Tuskailin pitkään miten saisin korjattua tämän haavoittuvuuden koodista. Löysin listan eri python ohjelmista ja tutkin niitä tuloksetta. En osannut löytää virhettä koodista, jolla voisin tukkia haavoittuvuuden.
<img width="1132" height="1254" alt="image" src="https://github.com/user-attachments/assets/24176baf-8074-4004-be8c-a3e97eabda8a" />

Jouduin lopulta tukeutumaan vihjeeseen, josta löytyi "hats" kansiosta "views.py" tiedosto, johon piti viimeiseen funktioon tehdä muutos joka varmistaa, että käyttäjällä on oikeat oikeudet varmasti. 
<img width="1744" height="950" alt="fuff1" src="https://github.com/user-attachments/assets/ab323f7a-f68e-4708-b03f-cce787648ace" />
Tässä näkyy muutoksen jälkeen lopputulos, kuinka nyt piilotetun hakemiston lisääminen palauttaa 403-sivun ja ei johda enään vanhaan paikkaan, joka oli harjoituksen haavoittuvuus.
<img width="2880" height="1538" alt="image" src="https://github.com/user-attachments/assets/1b66bf60-5b9d-412c-8419-53ee3bad402b" />
<img width="2144" height="828" alt="image" src="https://github.com/user-attachments/assets/945c0e06-ce17-4965-80ea-7d54ab951d5f" />

### Yhteenveto ffuf:sta
* Tämä oli työkaluna itselleni teoriatasolla tuttu, vaikka en ole aiemmin juuri tätä ohjelmaa käyttänyt. Olen aiemmin TryHackMe ja HackTheBox nimisissä palveluissa harjoitellut vapaa-ajalla hyökkäävän tietoturvan alkeita ja siellä olen käyttänyt vastaavia ohjelmia kuten GoBuster ja DirBuster. Näiden toiminta periaate on sama. Puolestaan korjaaminen oli todella paljon vaikeampaa. Siihen tarvitsin vihjeistä apua, mutta ymmärsin toiminta logikaan hyvin lopulta. Itsehaavoittuvuus tässä kuitenkin pohjuitui heikkoon access controlliin, eikä siihen, että piilotettu hakemisto oli mahdollinen löytää. Tämä tehtävä oli itselle helpompi, mutta silti taitojani koetteleva.



Lähteet:
- Karvinen, T. 2023. Find Hidden Web Directories - Fuzz URLs with ffuf. Luettavissa:https://terokarvinen.com/2023/fuzz-urls-find-hidden-directories/. Luettu: 1.9.2026.
- Karvinen, T. 2024. Hack'n Fix. Luettavissa:https://terokarvinen.com/hack-n-fix/. Luettu: 1.9.2026.
- OWASP 2021. A01:2021 – Broken Access Control. Luettavissa:https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/index.html. Luettu: 31.8.2026.
- PortSwigger 2026. Access control vulnerabilities and privilege escalation. Luettavissa:https://portswigger.net/web-security/access-control. Luettu: 31.8.2026.
- StackOverflow 2024. SQL: Two select statements in one query. Luettavissa:https://stackoverflow.com/questions/31979008/sql-two-select-statements-in-one-query. Luettu: 31.8.2026.
- w3schools 2026. SQL UNION Operator. Luettavissa:https://www.w3schools.com/sql/sql_union.asp. Luettu: 31.8.2026.



# h4 Some Disassembly Required

## x) Read/watch/listen and summarize.
- Ghidra on käänteismallintamiseen käytetty työkalu
- Videossa demonstroidaan ghidran toimintaa ja miten sitä käytetään
- Ohjelmia voidaan kääntää C-kieliseksi lähdekoodiksi
- Videolla ratkaistaan PicoCTF haaste

## a) Install Ghidra

Tehtävän aloitin päivittämällä paketti listan
````
sudo apt-get update
````
Sen jälkeen asensin Ghidran koneelleni.
````
sudo apt-get install ghidra
````
<img width="2091" height="1422" alt="image" src="https://github.com/user-attachments/assets/1f000194-5297-4253-9e63-c80be9fd2160" />

Ghidra asentui hakemistoon /usr/share/ghidra
````
cd /usr/share/ghidra/
````

Tämän jälkeen ajoin Ghidran.
````
./ghidraRun
````
Näin Ghidra lähti käyntiin.

<img width="1568" height="1024" alt="image" src="https://github.com/user-attachments/assets/f1cf621a-0f93-4719-a65d-44b9516c7d2e" />




## b) rever-C.

Ghidrassa liitin tehtävä tiedoston mukaan ja tämän jälkeen tarkoitus oli lähteä analysoimaan sitä.

<img width="1997" height="1131" alt="image" src="https://github.com/user-attachments/assets/9a2b7f4c-d4a3-482d-9cca-c45bf4c07ea6" />

Tässä kohdassa olin avannut avannut main funktion ja decompilerin avulla tutkin ohjelma koodia. 

<img width="413" height="409" alt="image" src="https://github.com/user-attachments/assets/48594f67-66f3-4405-8d90-36e4d1c4664e" />
<img width="2879" height="1608" alt="image" src="https://github.com/user-attachments/assets/a72d682d-a1a1-48ee-b5a6-e06ac2572074" />

Ohjelmakoodista kuva.

<img width="795" height="379" alt="image" src="https://github.com/user-attachments/assets/f15d07d6-d5dd-4403-b89e-b87f92f63e98" />

Tässä olin muuttanut pari muuttujaa toisiin. Tässä en ollut aivan varma, miten ja mitkä muuttujat tulisi vaihtaa niin hyödynsin Copilot (smart) apunani tässä tulkinassa. Aiemmat muuttuja nimet olivat epäselviä ja nyt selkeät.

````
local_28 --> password_input
````

````
iVar1 --> compare_result
````

<img width="798" height="368" alt="image" src="https://github.com/user-attachments/assets/13610f6e-6c4a-472f-bba6-261bce655db8" />

Ohjelma itse kysyy käyttäjän salasanaa ja vertaa sitä kovakoodattuun salasanaan. Mikäli syöte vastaa kovakoodattua salasanaa, niin tulosteena tulee flägi. Puolestaan jos ei vastaa kovakoodattua salasanaa, niin tulostaa virheen.

````
salasana: piilos-AnAnAs --> flag: FLAG{Tero-0e3bed0a89d8851da933c64fefad4ff2}");
````

## c) If backwards.

Aloitin avaamalla tiedoston Ghidrassa.

<img width="2880" height="1556" alt="image" src="https://github.com/user-attachments/assets/56801c94-122b-4911-9b55-4ae876cfdc0e" />

Minulla ei ollut ideaa kuinka lähteä ratkaisemaan haastetta ja jouduin katsomaan mallista ratkaisun tehtävään. Tässä muokattiin JNZ muotoon JZ, joka pyörättää ohjelman toimimaan päinvastaisella logiikalla.

<img width="1088" height="588" alt="image" src="https://github.com/user-attachments/assets/95f75ef0-99f8-4b6e-a0d7-d43d04646f29" />

Sitten muokkauksen jälkeen exporttasin muokatun filen ja lähdin ajamaan sitä.

<img width="1498" height="56" alt="image" src="https://github.com/user-attachments/assets/b57ba32e-4b0d-4884-9720-ae8eb407656d" />

Tässä ilmenee, että ohjelma toimii käänteisellä logiikalla. 

<img width="1812" height="312" alt="image" src="https://github.com/user-attachments/assets/d1bc321c-2b6a-4916-ae64-7898af93f629" />
<img width="1314" height="306" alt="image" src="https://github.com/user-attachments/assets/6130d2ac-ca24-4b07-87d1-09de8b0a625b" />


## d) Nora CrackMe.

Kloonasin Nora CrackMe tiedostot koneelle.
````
git clone https://github.com/NoraCodes/crackmes.git
````
<img width="1842" height="596" alt="image" src="https://github.com/user-attachments/assets/1eb7f728-5949-445b-b3b1-fe7731eecd26" />

Näkymä, kun kaikki tiedostot kloonattu.

<img width="1768" height="938" alt="image" src="https://github.com/user-attachments/assets/4b18dc34-3871-4df6-a2fa-e81b683596fc" />

Käänsin komennolla ```` make ```` tiedoston binääriksi.

<img width="1870" height="364" alt="image" src="https://github.com/user-attachments/assets/170a1fdd-e6c2-46d5-b89e-3ffa821f7ed1" />


## e) Nora crackme01.

Avasin harjoitus tiedoston Ghidrassa ja tarkastellessani main funktiota, niin sieltä paljastui salasana, jota testasin ja se toimi ensimmäisellä yrityksellä.

<img width="2262" height="990" alt="image" src="https://github.com/user-attachments/assets/fd2eaa32-1bfb-4d05-b854-a6fb6cb439ca" />
<img width="1324" height="194" alt="image" src="https://github.com/user-attachments/assets/553e52fc-48b5-43e5-9a1b-91846a85a0ba" />


## e) Nora crackme01e.

Tässä lähdin ratkomaan samalla tavalla ja löysin salasanan, mutta se ei toiminut. Jouduin kysymään apua Copilot AI (smart), joka vihjasi, että "!" rikkoo salasanan syötteen aikana. Tätä varten tuli lisätä hipsukat, jotta salasana pystyi ajamaan kokonaisena ohjelmalle. Lopulta samalla salasanalla tehtävä ratkesi.

<img width="732" height="600" alt="image" src="https://github.com/user-attachments/assets/7694cb5f-73b6-4807-b333-093495b106c0" />
<img width="1338" height="380" alt="image" src="https://github.com/user-attachments/assets/e468d1cd-c590-4e2b-980b-0fdd23b04169" />


## f) Nora crackme02

Viimeinen haaste oli jo todella haasteellinen itselle, kun pelkkä salasana, joka löytyi koodista ei toiminut. Jouduin katsomaan walktrough videon YouTubesta, josta selvisi ratkaisu menetelmät tämän ratkaisuun. Menetelmä oli itselle täysin uusi ja pyrin ymmärtämään ratkaisijan ajatusmaailmaa ratkaisemisen aikana.

<img width="718" height="696" alt="image" src="https://github.com/user-attachments/assets/d76eb65f-523a-4481-8e6e-12c5561471b3" />
<img width="1334" height="210" alt="image" src="https://github.com/user-attachments/assets/5346c928-8263-49ff-9f85-b27b6163d0c7" />
<img width="1296" height="194" alt="image" src="https://github.com/user-attachments/assets/96759ee2-7fe2-4d70-9053-b3455fe3c292" />




## Lähteet: 
- Copilot AI (smart)
- Fath, A. 28.6.2025. crackme02 - NoraCrackmes penyelesaian. Al Fath. YouTube. Katsottavissa: https://www.youtube.com/watch?v=0QnBlUgee5E. Katsottu: 15.9.2026.
- Hammond, J. 27.4.2022. GHIDRA for Reverse Engineering (PicoCTF 2022 #42 'bbbloat'). John Hammond. YouTube. Katsottavissa: https://www.youtube.com/watch?v=oTD_ki86c9I. Katsottu: 15.9.2026.
- Karvinen, T. 2026. Sovellusten hakkerointi. Luettavissa: https://terokarvinen.com/application-hacking/. Luettu: 15.9.2026.

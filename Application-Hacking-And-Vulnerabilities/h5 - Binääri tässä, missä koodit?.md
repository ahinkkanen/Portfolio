# h5 Binääri tässä, missä koodit?

## lab0.zip
Aloitin lataamalla harjoitus materiaalin Moodlesta ja siirsin sen kurssin kansioon. ````Dynaaminen analyysi-20260917.zip````. Tämän jälkeen purin harjoitustiedoston, josta avautui yksittäisten tehtävien zip-tiedostot. Purin ne ````unzip Dynaaminen analyysi-20260917.zip```` ja ````unzip lab0.zip````.

<img width="1776" height="394" alt="image" src="https://github.com/user-attachments/assets/b045aeae-b3c4-41a4-8487-b8c4ef8b8d3a" />
Lab0 löytyi buggy_program, jonka käänsin debuggeria varten ajettavaksi ohjelmaksi. Tämän tein komennolla 

````g++ buggy_program.c -g -Wall -Werror -o buggy-dbg````.

<img width="1340" height="204" alt="image" src="https://github.com/user-attachments/assets/541ec25b-60da-43e2-b7b4-2b595ca947ff" />

Tässä nähdään, että ohjelmassa alunperin elementit eivät täsmänneet toistensa kanssa.
<img width="1284" height="448" alt="image" src="https://github.com/user-attachments/assets/16535d57-f507-4f06-a2b0-79fd3ee424fd" />

Otin debuggerin käyttöön debuggausta varten luomalleni tiedostolle ja sieltä tein koodiin muutoksen, jossa määritin kokonaisluku määrän uusiksi ja lisäsin "0" merkkijonon alkuun. Sitten vielä käänsin ohjelman uudestaan ja sitten ohjelma toimi kuin halusin ````g++ buggy_program.c -g -Wall -Werror -o buggy-dbg````.

<img width="2084" height="1340" alt="image" src="https://github.com/user-attachments/assets/b280873d-635a-4c2f-bb27-6fc4aa82a50e" />
<img width="1438" height="428" alt="image" src="https://github.com/user-attachments/assets/dc4e614b-8d75-4e72-86e1-f1a45bc9bc66" />

Tässä vielä micro editorista kuva, jossa tein itse koodin muokkaamisen.
<img width="2116" height="864" alt="image" src="https://github.com/user-attachments/assets/5771545b-2b24-4d69-b777-0e2706bf4d76" />


## lab1.zip

Aloitin samalla tavalla unzippaamalla lab1.zip tiedoston ja lähdin ajamaan ohjelmaa, joka löytyi tiedostosta.
<img width="750" height="196" alt="image" src="https://github.com/user-attachments/assets/babba1e2-6f68-4c4d-b16c-2c0bf52978ff" />

Yritin ajaa ohjelmaa, mutta näytti vain kaatuvan.
<img width="1484" height="230" alt="image" src="https://github.com/user-attachments/assets/b3c5ae69-407f-4559-8c9f-0b3fe57c4ffe" />

Käänsiin taas lähdekoodin debuggausta varten ajettavaksi ohjelmaksi ja läähdin selvittämään tilannetta. 

````
gcc gdb_example1.c -g -Wall -Werror -o gdb_example1-dbg

````
<img width="1596" height="222" alt="image" src="https://github.com/user-attachments/assets/56b4adf6-9c01-4c2d-bd35-96fec5e8864e" />

Ajoin ohjelman debuggerissa komennolla ````run````. Sieltä selviää SIGSEGV, jossa ohjelma pysähtyy tismalleen kaatumiskohtaan. Rivin 7. kohta ````printf("%c", (*message)+i);````
<img width="2070" height="1448" alt="image" src="https://github.com/user-attachments/assets/3b3b3497-8210-45d5-8bdf-e2fe42977ed3" />

Avasin ````layout split```` komennolla tämän. Täällä myös huomasin saman ongelman. Käytin Copilot AI (smart) tekemään koodiin muutoksen, koska kieli itselle vieras. 
<img width="1994" height="1030" alt="image" src="https://github.com/user-attachments/assets/d97ec12e-793b-498c-9bd3-b8b8bcb7ccc5" />
<img width="2180" height="1140" alt="image" src="https://github.com/user-attachments/assets/634c5fea-0c0d-48bf-b10a-640676ec42d3" />

Muokattu koodi.
<img width="1556" height="1390" alt="image" src="https://github.com/user-attachments/assets/d932c334-586c-4d58-aa18-87d54f75ab5d" />


Tämän muutoksen jälkeen taas käänsin ohjelman uudelleen ja se se ei tulostanut samaa virhettä, kuin aiemmin. 

<img width="1382" height="434" alt="image" src="https://github.com/user-attachments/assets/041dc88e-c6fa-4ad4-b2f5-0fffa6c0ca6b" />




## lab2.zip

Tein samat purkamis toimenpiteet, kuin aiemmin myös tehtävien alussa ja navigoin itseni oikean tehtävä kansioon. Sitten lähdin debuggaamaan ohjelmaa.
<img width="1122" height="284" alt="image" src="https://github.com/user-attachments/assets/8fe0ab5d-eadd-4b2e-8350-a448b46e0845" />


Aloitin homman tutkimalla main-funktioita kutsumalla sitä debuggerissa ````disassemble /r main````. Parametri /r mahdollistaa normaalin assemblyn lisäksi myös bittikoodin tulkitsemisen.

<img width="1288" height="1156" alt="image" src="https://github.com/user-attachments/assets/fcff5ddf-5ff7-48f3-b35c-812bcdec2260" />

Tutkin komennolla ````disassemble mAsdf3a```` itse ````mAsdf3a```` -funktiota.

<img width="1360" height="1308" alt="image" src="https://github.com/user-attachments/assets/506009f4-a334-41e2-a66a-a776650ed190" />

Sieltä löytyi mielenkiintoisia kutsuja, joihin asetin breakpointteja, mutta alkuun niistä ei saanut mitään hyötyä, kun laitoin ohjeman käyntiin. Kunnes suoritin breakpointin kutsulle mAsdf3a komennolla ````break mAsdf3a```` ja poistin ````delete```` aiemmat breakpointit. Nyt pääsin syöttämään omaa salasanaa ohjelmalle debuggerissa ja sen jälkeen komennolla ````x/s $rdi```` sainkin käännettyä ohjelmasta ulos kovakoodatun salasanan ````anLTj4u8````.

<img width="1430" height="256" alt="image" src="https://github.com/user-attachments/assets/bc7e8685-4e27-4e72-86d7-541d86b83c63" />
<img width="1672" height="790" alt="image" src="https://github.com/user-attachments/assets/b207b68c-0f45-4fbc-8665-0e42e202e12b" />

Tarkoitus oli lähteä purkamaan kova koodattu salasana ````ASCII```` taulukon avulla. Tämä taulukko saatiin Kalissa auki terminaalissa komennolla ````man ascii````. Tarkoitus oli noudattaa ````mAsdf3a-funktion```` logiikkaa, jossa parilliseen indeksiin lisätään ````+3```` ja parittomaan ideksiin tehdään vähennys ````-7````.

<img width="2248" height="1418" alt="image" src="https://github.com/user-attachments/assets/66e60e39-54f8-4f99-9332-e58ddda4bff6" />
<img width="1328" height="146" alt="image" src="https://github.com/user-attachments/assets/876b37a3-0fd1-4695-9f1b-9a43769ee4dd" />

Tästä saatiin purettua tuolla logiikalla salasanaksi ````dgOMm-x1````

Seuraavaksi tarkoituksenani oli kokeilla salasanan toimivuutta ohjelmalle. Sieltä löytyikin haluttu lippu ````FLAG{Lari-rsvRDx04WMBZpuwg4qfYwzdcvVa0oym}````.

<img width="1220" height="190" alt="image" src="https://github.com/user-attachments/assets/a4e62a76-052d-4c83-ab0c-34921c1526fd" />

- Tehtävä oli todella haastava itselle ja aikaa kului paljon. Harjoituksen aikana opin selkeämmin käyttämään breakpointteja ja ajaa ohjelmaa. Myös uusia paratereja seka ascii taulukon käyttöä tuli opittua.


## lab3.zip

Purin tiedoston ja valitsin sieltä ensimmäisen haasteen. Käänsin tämän ohjelman koodin ajettavaksi ohjelmaksi debuggausta varten. Komennolla ````gcc crackme01.c -g -Wall -Werror -o crackme01.c-dbg````. Sitten lähdin debuggaamaan kääntämääni ohjelmaa ````dbg crackme01.c-dbg````.

<img width="2170" height="986" alt="image" src="https://github.com/user-attachments/assets/84bff468-ae5b-43a4-b71a-7274f105225b" />

Avasin ````layout split```` näkymän ja siellä ohjelma koodissa löytyi salasana ````password1````.

<img width="1640" height="816" alt="image" src="https://github.com/user-attachments/assets/baeda442-9b74-42dd-bb78-579863d10299" />

<img width="2036" height="1110" alt="image" src="https://github.com/user-attachments/assets/ac6a1b93-5cc2-47a9-aefa-cd4f4eb38b36" />

Lähdin kokeilemaan löytämääni salasanaa ensiksi kääntämälleni ohjelmalle ja sitten alkuperäiselle. Molemmat toimivat onnistuneesti.

<img width="1258" height="326" alt="image" src="https://github.com/user-attachments/assets/4d666161-a609-41f2-932c-ca8ee4c341bb" />


## Lähteet:

- Copilot AI (smart), C-koodin muokkaus.
- Karvinen, T. 2026. Sovellusten hakkerointi. Luettavissa: https://terokarvinen.com/application-hacking/. Luettu: 21.9.2026.

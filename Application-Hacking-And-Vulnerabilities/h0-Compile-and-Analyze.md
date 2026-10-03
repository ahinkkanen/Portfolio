# h0 Compile and Analyze

a)

Tehtävässä käytin Kali Linux virtuaalikonetta. Aloitin tehtävän luomalla tekstitiedoston hyödyntäen nano-tekstieditoria. 
````
nano testi.c
````
<img width="677" height="312" alt="image" src="https://github.com/user-attachments/assets/7f4e7391-06ae-47df-8ded-614231c382e4" />


Editorin sisälle kirjoitin yksinkertaiset C-kielisen ohjelman, jonka tarkoitus oli tulostaa "Hello, World!".


````
#include <stdio.h>
int main() {
   printf("Hello, World!\n");
   return 0;
}
````

<img width="1436" height="576" alt="image" src="https://github.com/user-attachments/assets/0e88e8b3-44fa-4aad-9c2e-d7a8a972f5cb" />


Seuraavaksi käänsin kirjoittamani C-koodin ohjelmaksi nimeltä "a.out". Tein tämän hyödyntäen valmiina Linuxissani olevaa GCC-compiler työkalua.
````
gcc testi.c
````
<img width="2120" height="391" alt="image" src="https://github.com/user-attachments/assets/a5469903-08d2-410e-8be1-1378b6a9ded3" />


<img width="619" height="121" alt="image" src="https://github.com/user-attachments/assets/81347af9-0128-4119-bc8d-91eb03496878" />



Nyt kotihakemistooni oli ilmestynyt "a.out", joka on compilerin kääntämä ohjelma.
<img width="1793" height="321" alt="image" src="https://github.com/user-attachments/assets/57a8312c-44e3-4bd7-b294-fd9973c258f1" />

Komento "file" tutki binäärin rakennetta ja palautti minulle ohjelmasta tietoa.
````
file a.out
````
<img width="2176" height="324" alt="image" src="https://github.com/user-attachments/assets/b5f283a3-1b1d-4484-8ca7-37effcda0c41" />


Lopuksi testasin vielä ohjelmani toimivuutta onnistuneesti.
<img width="849" height="503" alt="image" src="https://github.com/user-attachments/assets/a2d1b6a4-66c3-47c0-b974-eeb0e2edcb68" />



Lähteet:
* Karvinen, T. 2023. Create a Web Page Using Github. Luettavissa: https://terokarvinen.com/2023/create-a-web-page-using-github/. Luettu: 20.8.2026
* Karvinen, T. 2026. Sovellusten hakkerointi. Luettavissa: https://terokarvinen.com/application-hacking/. Luettu: 20.8.2026
* Parewa Labs Pvt. C "Hello, World!" Program. Luettavissa: https://www.programiz.com/c-programming/examples/print-sentence. Luettu: 20.8.2026.
